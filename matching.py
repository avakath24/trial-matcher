"""
Matching engine for the AI-Powered Clinical Trial Matching System.

Design (the key improvement over a naive "embed everything and rank" approach):

1. HARD FILTERS first -- age range, sex, and condition/diagnosis match.
   These are non-negotiable eligibility facts, not "vibes." A 15-year-old
   should never be ranked against an adults-only trial just because the
   text is semantically similar.

2. SEMANTIC SIMILARITY second -- only among trials that pass the hard
   filters, we use sentence embeddings to score how well the patient's
   free-text history matches the trial's inclusion/exclusion criteria.
   This is where the "fuzzy" matching value comes in (e.g. matching
   "no prior treatment" to "treatment naive" even with different wording).

3. EXPLAINABILITY -- for each match, we identify and surface the single
   most similar criterion sentence, so the output isn't a black-box score.
"""

from functools import lru_cache

import numpy as np
from sentence_transformers import SentenceTransformer

from data.trials import get_all_trials, get_trial_text
from data.patients import get_patient_text


@lru_cache(maxsize=1)
def get_model():
    # all-MiniLM-L6-v2 is small, fast, and well-suited for semantic similarity
    # tasks like this -- a good default choice for a project like this.
    return SentenceTransformer("all-MiniLM-L6-v2")


def passes_hard_filters(patient: dict, trial: dict) -> tuple[bool, list[str]]:
    """Returns (passes, reasons_failed)."""
    reasons = []

    if not (trial["min_age"] <= patient["age"] <= trial["max_age"]):
        reasons.append(
            f"Age {patient['age']} is outside trial's allowed range "
            f"({trial['min_age']}-{trial['max_age']})"
        )

    if trial["sex"] != "ALL" and trial["sex"] != patient["sex"]:
        reasons.append(f"Trial requires sex={trial['sex']}, patient is {patient['sex']}")

    # Condition match: require meaningful keyword overlap between patient
    # diagnosis and trial condition (simple but effective hard gate before
    # we even consider semantic similarity on the fuzzy stuff).
    patient_dx_words = set(patient["diagnosis"].lower().split())
    trial_cond_words = set(trial["condition"].lower().split())
    overlap = patient_dx_words & trial_cond_words
    # Require at least one meaningful overlapping word (ignore generic words)
    generic = {"the", "of", "and", "or", "with", "in", "non", "-"}
    meaningful_overlap = overlap - generic
    if not meaningful_overlap:
        reasons.append(
            f"Diagnosis '{patient['diagnosis']}' does not match trial condition '{trial['condition']}'"
        )

    return (len(reasons) == 0, reasons)


def find_most_similar_criterion(patient_embedding, trial: dict, model) -> tuple[str, float]:
    """Finds which single inclusion/exclusion sentence is most similar to the patient text."""
    criteria = trial["inclusion"] + trial["exclusion"]
    if not criteria:
        return ("(No specific criteria listed beyond condition match)", 0.0)

    criteria_embeddings = model.encode(criteria, convert_to_numpy=True, normalize_embeddings=True)
    sims = criteria_embeddings @ patient_embedding
    best_idx = int(np.argmax(sims))
    return (criteria[best_idx], float(sims[best_idx]))


def match_patient_to_trials(patient: dict, top_k: int = 5) -> list[dict]:
    """
    Main entry point. Returns a ranked list of trial matches with scores,
    explanations, and hard-filter status for every trial (including the
    ones that failed filters, so the UI can show why they were excluded).
    """
    model = get_model()
    trials = get_all_trials()

    patient_text = get_patient_text(patient)
    patient_embedding = model.encode(patient_text, convert_to_numpy=True, normalize_embeddings=True)

    results = []
    for trial in trials:
        passed, fail_reasons = passes_hard_filters(patient, trial)

        if not passed:
            results.append({
                "trial": trial,
                "eligible": False,
                "fail_reasons": fail_reasons,
                "similarity_score": None,
                "best_matching_criterion": None,
            })
            continue

        trial_text = get_trial_text(trial)
        trial_embedding = model.encode(trial_text, convert_to_numpy=True, normalize_embeddings=True)
        overall_similarity = float(trial_embedding @ patient_embedding)

        best_criterion, criterion_score = find_most_similar_criterion(patient_embedding, trial, model)

        results.append({
            "trial": trial,
            "eligible": True,
            "fail_reasons": [],
            "similarity_score": overall_similarity,
            "best_matching_criterion": best_criterion,
            "best_criterion_score": criterion_score,
        })

    # Sort: eligible trials first (by similarity score descending), then ineligible
    eligible = sorted(
        [r for r in results if r["eligible"]],
        key=lambda r: r["similarity_score"],
        reverse=True,
    )
    ineligible = [r for r in results if not r["eligible"]]

    return (eligible[:top_k], ineligible)
