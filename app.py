"""
AI-Powered Clinical Trial Matching System -- Streamlit app.

Run with:
    streamlit run app.py
"""

import streamlit as st

from data.patients import get_all_patients
from data.trials import get_all_trials
from matching import match_patient_to_trials

st.set_page_config(page_title="Clinical Trial Matcher", page_icon="🧬", layout="wide")

st.title("🧬 AI-Powered Clinical Trial Matching System")
st.caption(
    "Matches synthetic patient profiles to real ClinicalTrials.gov studies using hard "
    "eligibility filters (age, sex, diagnosis) plus semantic similarity (sentence embeddings) "
    "on the fuzzier criteria — not a black box: every match shows which specific criterion drove it."
)

with st.expander("⚠️ Important: read before using"):
    st.markdown(
        "- **This is a portfolio/demonstration project, not a clinical decision-making tool.** "
        "Patient profiles are entirely synthetic.\n"
        "- Trial data is real (sourced from ClinicalTrials.gov), but eligibility criteria have "
        "been condensed for this demo — always check the full official trial record before any "
        "real-world decision.\n"
        "- This tool does not replace a clinician, research coordinator, or the official "
        "ClinicalTrials.gov eligibility review process."
    )

patients = get_all_patients()
trials = get_all_trials()

st.sidebar.title("🧬 Trial Matcher")
st.sidebar.markdown(f"**{len(trials)}** real trials in database\n\n**{len(patients)}** synthetic patient profiles")
st.sidebar.markdown("---")

mode = st.sidebar.radio("Mode", ["Pick a sample patient", "Enter custom patient"])

if mode == "Pick a sample patient":
    patient_options = {f"{p['id']} — {p['name']} ({p['diagnosis']}, age {p['age']})": p for p in patients}
    selected_label = st.sidebar.selectbox("Patient", list(patient_options.keys()))
    patient = patient_options[selected_label]
else:
    st.sidebar.markdown("**Enter patient details:**")
    name = st.sidebar.text_input("Name/ID", "Custom Patient")
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=45)
    sex = st.sidebar.selectbox("Sex", ["FEMALE", "MALE"])
    diagnosis = st.sidebar.text_input("Diagnosis", "HER2-positive Breast Cancer")
    stage = st.sidebar.text_input("Stage/Substage", "Stage II")
    biomarkers = st.sidebar.text_input("Biomarkers", "HER2 IHC 3+")
    history = st.sidebar.text_area("Relevant medical history", "Newly diagnosed, no prior treatment.")
    patient = {
        "id": "CUSTOM",
        "name": name,
        "age": age,
        "sex": sex,
        "diagnosis": diagnosis,
        "stage_or_substage": stage,
        "biomarkers": biomarkers,
        "history": history,
    }

top_k = st.sidebar.slider("Number of top matches to show", 1, 10, 5)

# ---------- Patient summary ----------
st.subheader(f"Patient profile: {patient['name']}")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Age", patient["age"])
col2.metric("Sex", patient["sex"])
col3.metric("Diagnosis", patient["diagnosis"])
col4.metric("Stage", patient["stage_or_substage"])
st.markdown(f"**Biomarkers:** {patient['biomarkers']}")
st.markdown(f"**History:** {patient['history']}")

st.markdown("---")

# ---------- Run matching ----------
with st.spinner("Embedding patient profile and scoring against trial database..."):
    eligible, ineligible = match_patient_to_trials(patient, top_k=top_k)

st.subheader(f"✅ Top {len(eligible)} matching trials")

if not eligible:
    st.warning("No trials passed the hard eligibility filters for this patient profile.")
else:
    for rank, r in enumerate(eligible, start=1):
        trial = r["trial"]
        with st.container(border=True):
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.markdown(f"**#{rank}. {trial['title']}**")
                st.caption(f"NCT ID: {trial['nct_id']} | Phase: {trial['phase']} | Condition: {trial['condition']}")
            with col_b:
                st.metric("Match score", f"{r['similarity_score']*100:.1f}%")

            st.markdown(f"🎯 **Most relevant criterion:** _{r['best_matching_criterion']}_")

            with st.expander("Full eligibility criteria"):
                st.markdown(f"**Age range:** {trial['min_age']}–{trial['max_age']} | **Sex:** {trial['sex']}")
                if trial["inclusion"]:
                    st.markdown("**Inclusion criteria:**")
                    for c in trial["inclusion"]:
                        st.markdown(f"- {c}")
                if trial["exclusion"]:
                    st.markdown("**Exclusion criteria:**")
                    for c in trial["exclusion"]:
                        st.markdown(f"- {c}")
                st.markdown(f"[View full trial record on ClinicalTrials.gov →](https://clinicaltrials.gov/study/{trial['nct_id']})")

st.markdown("---")
with st.expander(f"❌ Trials excluded by hard filters ({len(ineligible)})"):
    for r in ineligible:
        trial = r["trial"]
        st.markdown(f"**{trial['nct_id']} — {trial['title']}**")
        for reason in r["fail_reasons"]:
            st.markdown(f"- {reason}")
        st.markdown("")

st.markdown("---")
st.caption(
    "Trial data sourced from real ClinicalTrials.gov study records (see README for full provenance notes). "
    "Patient profiles are synthetic. Matching uses sentence-transformers (all-MiniLM-L6-v2) for semantic "
    "similarity, combined with hard eligibility filters for age, sex, and diagnosis."
)
