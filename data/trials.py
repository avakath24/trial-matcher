"""
Clinical trial dataset for the AI-Powered Clinical Trial Matching System.

DATA PROVENANCE:
All trials below are real, currently/recently listed studies from
ClinicalTrials.gov (https://clinicaltrials.gov), identified by their real
NCT ID. Eligibility criteria, age/sex restrictions, and conditions are taken
from each trial's actual published record. Criteria text has been lightly
condensed/reformatted into structured fields (inclusion list, exclusion list,
hard filters) for this project, but the substance is drawn from the real
published eligibility sections, not invented.

Note: ClinicalTrials.gov's bulk API (api/v2/studies) was not reachable from
this build environment, so trials were sourced individually by searching
and reading each study's public page.

Covers three conditions to give the matcher meaningful variety:
- Multiple Sclerosis (relapsing forms)
- HER2-positive Breast Cancer
- Non-Small Cell Lung Cancer (NSCLC), especially EGFR-mutated
"""

TRIALS = [
    # ---------------- Multiple Sclerosis ----------------
    {
        "nct_id": "NCT01464905",
        "title": "Phase 3 Study of NU100 in Relapsing Forms of Multiple Sclerosis (RRMS)",
        "condition": "Relapsing-Remitting Multiple Sclerosis",
        "phase": "Phase 3",
        "min_age": 18,
        "max_age": 60,
        "sex": "ALL",
        "inclusion": [
            "Diagnosis of relapsing-remitting multiple sclerosis (RRMS) per McDonald Criteria (2010 revision)",
            "Interferon beta-1b naive (no prior treatment with this drug class)",
            "Expanded Disability Status Scale (EDSS) score below 5.5",
        ],
        "exclusion": [
            "Medical or psychiatric conditions that compromise ability to participate or complete the study safely",
        ],
    },
    {
        "nct_id": "NCT04879628",
        "title": "Frexalimab (SAR441344) Proof-of-Concept Study in Relapsing Multiple Sclerosis",
        "condition": "Relapsing Multiple Sclerosis",
        "phase": "Phase 2",
        "min_age": 18,
        "max_age": 55,
        "sex": "ALL",
        "inclusion": [
            "Diagnosis of relapsing forms of multiple sclerosis",
            "Evidence of recent disease activity (relapse or new MRI lesions) in the past 12 months",
        ],
        "exclusion": [
            "Primary progressive multiple sclerosis",
            "Significant cardiovascular, hepatic, or renal disease",
        ],
    },
    {
        "nct_id": "NCT02283853",
        "title": "BG00012 (Dimethyl Fumarate) in Pediatric Relapsing-Remitting Multiple Sclerosis",
        "condition": "Relapsing-Remitting Multiple Sclerosis",
        "phase": "Phase 3",
        "min_age": 10,
        "max_age": 17,
        "sex": "ALL",
        "inclusion": [
            "Body weight of at least 30 kg",
            "Diagnosis of RRMS using consensus pediatric criteria",
            "Ambulatory with baseline EDSS score between 0 and 5.5",
        ],
        "exclusion": [
            "Disease course showing continuous worsening over 3+ months without stable periods (suggests progressive rather than relapsing-remitting course)",
            "Disorders that mimic MS, such as other demyelinating diseases",
        ],
    },
    {
        "nct_id": "NCT05285891",
        "title": "Ocrelizumab Discontinuation Study in Relapsing Multiple Sclerosis",
        "condition": "Relapsing Multiple Sclerosis",
        "phase": "Phase 4",
        "min_age": 18,
        "max_age": 65,
        "sex": "ALL",
        "inclusion": [
            "Currently receiving ocrelizumab treatment for relapsing multiple sclerosis",
            "Stable disease course on current therapy",
        ],
        "exclusion": [
            "Primary progressive multiple sclerosis",
        ],
    },
    {
        "nct_id": "NCT07318129",
        "title": "Indole-3-Propionic Acid (IPA) Supplementation in Relapsing-Remitting MS",
        "condition": "Relapsing Remitting Multiple Sclerosis (RRMS)",
        "phase": "N/A (dietary supplement)",
        "min_age": 18,
        "max_age": 65,
        "sex": "ALL",
        "inclusion": [
            "Confirmed diagnosis of relapsing-remitting multiple sclerosis",
            "Willing to take daily oral capsules for 27 consecutive months",
        ],
        "exclusion": [
            "Known gastrointestinal disorders affecting nutrient absorption",
        ],
    },

    # ---------------- HER2-positive Breast Cancer ----------------
    {
        "nct_id": "NCT06603597",
        "title": "PRO-HER2: Prospective Evaluation of Outcomes for HER2-positive Breast Cancer",
        "condition": "HER2-positive Breast Cancer",
        "phase": "Observational",
        "min_age": 18,
        "max_age": 100,
        "sex": "ALL",
        "inclusion": [
            "Stage I-IV HER2-positive breast cancer",
        ],
        "exclusion": [],
    },
    {
        "nct_id": "NCT06762977",
        "title": "HERCard: Composite Genomic Assay for HER2-positive Early-Stage Breast Cancer",
        "condition": "Early-Stage HER2-positive Breast Cancer",
        "phase": "Observational",
        "min_age": 18,
        "max_age": 100,
        "sex": "FEMALE",
        "inclusion": [
            "Operable breast cancer, stage I-III",
            "HER2-positive primary tumor confirmed by IHC 3+ or 2+ with positive ISH amplification",
            "Received or planned neoadjuvant/adjuvant trastuzumab-based therapy",
        ],
        "exclusion": [
            "Follow-up period of less than 3 years after surgery",
        ],
    },
    {
        "nct_id": "NCT02162667",
        "title": "CT-P6 Biosimilar Trial in HER2-positive Early Breast Cancer",
        "condition": "HER2-positive Early Breast Cancer",
        "phase": "Phase 3",
        "min_age": 18,
        "max_age": 100,
        "sex": "FEMALE",
        "inclusion": [
            "Newly diagnosed, histologically confirmed breast cancer",
            "Clinical stage I, II, or IIIa operable breast cancer",
            "HER2-positive status confirmed locally (IHC 3+)",
        ],
        "exclusion": [
            "Bilateral breast cancer",
            "Prior treatment for breast cancer including chemotherapy, hormone therapy, radiation, or surgery",
        ],
    },
    {
        "nct_id": "NCT07376174",
        "title": "Prognostic Impact of HER2 Expression in Non-Metastatic HER2-positive Breast Cancer",
        "condition": "Non-Metastatic HER2-positive Breast Cancer",
        "phase": "Observational",
        "min_age": 18,
        "max_age": 100,
        "sex": "ALL",
        "inclusion": [
            "Pathologically confirmed primary breast cancer, clinical stage I-III",
            "HER2-positive status confirmed by FISH testing with available HER2/CEP17 ratio",
            "Received dual-target therapy (trastuzumab plus pertuzumab)",
            "Underwent curative-intent surgery",
        ],
        "exclusion": [
            "Distant metastasis (Stage IV) or contralateral breast cancer at diagnosis",
            "Previous anti-HER2 targeted therapy prior to dual-target treatment",
        ],
    },
    {
        "nct_id": "NCT05954143",
        "title": "BDC-1001 +/- Pertuzumab in HER2-Positive Metastatic Breast Cancer",
        "condition": "HER2-Positive Metastatic Breast Cancer",
        "phase": "Phase 1/2",
        "min_age": 18,
        "max_age": 100,
        "sex": "ALL",
        "inclusion": [
            "Metastatic HER2-positive breast cancer",
            "Measurable disease per RECIST criteria",
        ],
        "exclusion": [
            "Untreated or symptomatic central nervous system metastases",
        ],
    },

    # ---------------- Non-Small Cell Lung Cancer (NSCLC) ----------------
    {
        "nct_id": "NCT07379476",
        "title": "ATOM2: Local Ablative Therapy for Oligoresidual Metastasis in EGFR-Mutated NSCLC",
        "condition": "EGFR-Mutated Non-Small Cell Lung Cancer",
        "phase": "Phase 2",
        "min_age": 18,
        "max_age": 100,
        "sex": "ALL",
        "inclusion": [
            "Pathologically proven non-small cell lung cancer",
            "Positive for EGFR exon 19 deletion or exon 21 L858R mutation",
            "Stage IV disease",
            "Three or fewer active residual cancer sites after 3-6 months of first-line osimertinib treatment",
        ],
        "exclusion": [],
    },
    {
        "nct_id": "NCT03831932",
        "title": "Telaglenastat Plus Osimertinib in EGFR-Mutated Stage IV NSCLC",
        "condition": "EGFR-Mutated Stage IV Non-Small Cell Lung Cancer",
        "phase": "Phase 1/2",
        "min_age": 18,
        "max_age": 100,
        "sex": "ALL",
        "inclusion": [
            "Histologically confirmed stage IV NSCLC with advanced or metastatic disease",
            "Activating EGFR mutation (L858R or exon 19 deletion) confirmed by tissue biopsy",
            "Disease progression on most recent EGFR-targeted therapy",
        ],
        "exclusion": [
            "Eligibility cannot be determined from liquid (blood-based) biopsy alone",
        ],
    },
    {
        "nct_id": "NCT01998126",
        "title": "Checkpoint Inhibitor Plus Erlotinib/Crizotinib for EGFR or ALK Mutated Stage IV NSCLC",
        "condition": "EGFR or ALK Mutated Non-Small Cell Lung Cancer",
        "phase": "Phase 1",
        "min_age": 18,
        "max_age": 100,
        "sex": "ALL",
        "inclusion": [
            "Stage IV NSCLC, or stage II-III NSCLC not curable by standard techniques",
            "EGFR or ALK mutated NSCLC",
            "ECOG performance status of 0, 1, or 2",
        ],
        "exclusion": [
            "More than 6 months of prior targeted inhibitor treatment while disease is not progressing",
        ],
    },
    {
        "nct_id": "NCT01703091",
        "title": "Docetaxel and Ramucirumab vs Docetaxel and Placebo in Stage IV NSCLC",
        "condition": "Stage IV Non-Small Cell Lung Cancer",
        "phase": "Phase 3",
        "min_age": 18,
        "max_age": 100,
        "sex": "ALL",
        "inclusion": [
            "Clinical stage IV or recurrent NSCLC",
            "One prior first-line platinum-based chemotherapy regimen",
            "ECOG performance status 0 or 1",
            "Measurable disease per RECIST v1.1",
            "Estimated life expectancy of at least 3 months",
        ],
        "exclusion": [],
    },
    {
        "nct_id": "NCT01153399",
        "title": "REASON Study: EGFR Mutation Status Registry in Advanced/Metastatic NSCLC",
        "condition": "Locally Advanced or Metastatic Non-Small Cell Lung Cancer",
        "phase": "Observational",
        "min_age": 18,
        "max_age": 100,
        "sex": "ALL",
        "inclusion": [
            "Histologically confirmed locally advanced or metastatic NSCLC (stage IIIB/IV)",
            "Receiving first-line treatment for stage IIIB/IV NSCLC",
            "Known EGFR mutation status",
            "Tumor not amenable to curative surgery or radiotherapy",
        ],
        "exclusion": [
            "Mixed histology of small cell and non-small cell lung cancer",
        ],
    },
]


def get_all_trials():
    return TRIALS


def get_trial_text(trial: dict) -> str:
    """Builds a single text blob from a trial's criteria, used for embedding."""
    parts = [
        f"Condition: {trial['condition']}.",
        "Inclusion criteria: " + " ".join(trial["inclusion"]) if trial["inclusion"] else "",
        "Exclusion criteria: " + " ".join(trial["exclusion"]) if trial["exclusion"] else "",
    ]
    return " ".join(p for p in parts if p)
