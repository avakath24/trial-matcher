"""
Synthetic patient profiles for the AI-Powered Clinical Trial Matching System.

These are entirely fictional, invented for this project. Using synthetic
data instead of real patient records is the correct and necessary choice
here -- real patient data is protected health information (PHI) and using
it would raise serious privacy and compliance issues.

Each profile mirrors the kind of structured fields a clinical research
coordinator would actually have on hand: demographics, diagnosis, disease
stage, relevant biomarkers, and a short free-text history note (used for
the semantic-similarity side of the matching).
"""

PATIENTS = [
    {
        "id": "P001",
        "name": "Patient A",
        "age": 34,
        "sex": "FEMALE",
        "diagnosis": "Relapsing-Remitting Multiple Sclerosis",
        "stage_or_substage": "Early, low disability",
        "biomarkers": "EDSS 2.0, no recent relapse",
        "history": "Diagnosed 2 years ago, never treated with interferon beta-1b, stable on no current disease-modifying therapy.",
    },
    {
        "id": "P002",
        "name": "Patient B",
        "age": 15,
        "sex": "MALE",
        "diagnosis": "Relapsing-Remitting Multiple Sclerosis",
        "stage_or_substage": "Pediatric onset",
        "biomarkers": "EDSS 1.5, body weight 52 kg",
        "history": "Diagnosed at age 14, ambulatory, no signs of progressive disease course, currently untreated.",
    },
    {
        "id": "P003",
        "name": "Patient C",
        "age": 48,
        "sex": "FEMALE",
        "diagnosis": "Relapsing Multiple Sclerosis",
        "stage_or_substage": "Active disease",
        "biomarkers": "Two relapses and new MRI lesions in past year",
        "history": "Currently on ocrelizumab for the past 18 months with stable disease course, considering treatment options.",
    },
    {
        "id": "P004",
        "name": "Patient D",
        "age": 61,
        "sex": "FEMALE",
        "diagnosis": "Primary Progressive Multiple Sclerosis",
        "stage_or_substage": "Progressive course",
        "biomarkers": "Continuous worsening over past 8 months, no stable periods",
        "history": "Diagnosed with primary progressive MS, not a relapsing-remitting course.",
    },
    {
        "id": "P005",
        "name": "Patient E",
        "age": 29,
        "sex": "FEMALE",
        "diagnosis": "Relapsing-Remitting Multiple Sclerosis",
        "stage_or_substage": "Mild",
        "biomarkers": "EDSS 1.0",
        "history": "Newly diagnosed, interested in dietary supplement trials, no GI absorption disorders, willing to commit to multi-year studies.",
    },

    {
        "id": "P006",
        "name": "Patient F",
        "age": 52,
        "sex": "FEMALE",
        "diagnosis": "HER2-positive Breast Cancer",
        "stage_or_substage": "Stage II",
        "biomarkers": "HER2 IHC 3+, no prior breast cancer treatment",
        "history": "Newly diagnosed, operable tumor, has not yet started any chemotherapy, hormone therapy, or radiation.",
    },
    {
        "id": "P007",
        "name": "Patient G",
        "age": 67,
        "sex": "FEMALE",
        "diagnosis": "HER2-positive Breast Cancer",
        "stage_or_substage": "Stage IV (metastatic)",
        "biomarkers": "HER2-positive, measurable disease per RECIST",
        "history": "Metastatic at diagnosis, no central nervous system involvement, considering systemic therapy options.",
    },
    {
        "id": "P008",
        "name": "Patient H",
        "age": 45,
        "sex": "FEMALE",
        "diagnosis": "HER2-positive Breast Cancer",
        "stage_or_substage": "Stage III",
        "biomarkers": "HER2/CEP17 ratio available via FISH, completed dual-target therapy",
        "history": "Completed adjuvant trastuzumab plus pertuzumab, underwent curative-intent mastectomy, no distant metastasis at diagnosis.",
    },
    {
        "id": "P009",
        "name": "Patient I",
        "age": 39,
        "sex": "FEMALE",
        "diagnosis": "HER2-positive Breast Cancer",
        "stage_or_substage": "Stage I",
        "biomarkers": "HER2 IHC 3+, no prior anti-HER2 therapy",
        "history": "Early-stage disease, planned for neoadjuvant trastuzumab-based therapy, single breast involvement (not bilateral).",
    },
    {
        "id": "P010",
        "name": "Patient J",
        "age": 58,
        "sex": "MALE",
        "diagnosis": "HR-positive, HER2-negative Breast Cancer",
        "stage_or_substage": "Stage II",
        "biomarkers": "HER2 negative",
        "history": "Hormone receptor positive but HER2 negative disease, not eligible for HER2-targeted trials.",
    },

    {
        "id": "P011",
        "name": "Patient K",
        "age": 64,
        "sex": "MALE",
        "diagnosis": "Non-Small Cell Lung Cancer",
        "stage_or_substage": "Stage IV",
        "biomarkers": "EGFR exon 19 deletion confirmed via tissue biopsy",
        "history": "Progressed after first-line osimertinib, has 2 residual oligometastatic sites, ECOG performance status 1.",
    },
    {
        "id": "P012",
        "name": "Patient L",
        "age": 71,
        "sex": "FEMALE",
        "diagnosis": "Non-Small Cell Lung Cancer",
        "stage_or_substage": "Stage IV",
        "biomarkers": "EGFR exon 21 L858R mutation",
        "history": "First-line osimertinib for 4 months, currently has 1 active residual site amenable to local ablative therapy.",
    },
    {
        "id": "P013",
        "name": "Patient M",
        "age": 55,
        "sex": "MALE",
        "diagnosis": "Non-Small Cell Lung Cancer",
        "stage_or_substage": "Stage IIIB",
        "biomarkers": "EGFR mutation status unknown, awaiting biopsy results",
        "history": "Newly diagnosed, has not yet started first-line treatment, tumor not amenable to curative surgery.",
    },
    {
        "id": "P014",
        "name": "Patient N",
        "age": 60,
        "sex": "MALE",
        "diagnosis": "Non-Small Cell Lung Cancer",
        "stage_or_substage": "Stage IV",
        "biomarkers": "EGFR and ALK wild-type (no mutation detected)",
        "history": "Received one prior platinum-based chemotherapy regimen, ECOG performance status 1, measurable disease per RECIST v1.1.",
    },
    {
        "id": "P015",
        "name": "Patient O",
        "age": 49,
        "sex": "FEMALE",
        "diagnosis": "Non-Small Cell Lung Cancer",
        "stage_or_substage": "Stage IV",
        "biomarkers": "EGFR exon 19 deletion, only confirmed via blood-based liquid biopsy",
        "history": "Disease progression on osimertinib, no tissue biopsy yet performed, only liquid biopsy results available so far.",
    },

    {
        "id": "P016",
        "name": "Patient P",
        "age": 22,
        "sex": "FEMALE",
        "diagnosis": "Relapsing-Remitting Multiple Sclerosis",
        "stage_or_substage": "Early",
        "biomarkers": "EDSS 1.0, body weight 48 kg",
        "history": "Diagnosed at age 16 (pediatric onset), now an adult, ambulatory and stable.",
    },
    {
        "id": "P017",
        "name": "Patient Q",
        "age": 73,
        "sex": "MALE",
        "diagnosis": "HER2-positive Breast Cancer",
        "stage_or_substage": "Stage II",
        "biomarkers": "HER2 IHC 2+ with positive ISH amplification",
        "history": "Male breast cancer patient, operable tumor, planned for trastuzumab-based adjuvant therapy.",
    },
    {
        "id": "P018",
        "name": "Patient R",
        "age": 41,
        "sex": "FEMALE",
        "diagnosis": "Non-Small Cell Lung Cancer",
        "stage_or_substage": "Stage III",
        "biomarkers": "ALK translocation positive",
        "history": "Locally advanced disease, considering combination checkpoint inhibitor and targeted therapy trial.",
    },
    {
        "id": "P019",
        "name": "Patient S",
        "age": 36,
        "sex": "FEMALE",
        "diagnosis": "Relapsing Multiple Sclerosis",
        "stage_or_substage": "Active",
        "biomarkers": "Recent relapse 3 months ago",
        "history": "Considering switching from current therapy due to breakthrough disease activity.",
    },
    {
        "id": "P020",
        "name": "Patient T",
        "age": 66,
        "sex": "FEMALE",
        "diagnosis": "Non-Small Cell Lung Cancer",
        "stage_or_substage": "Stage IV",
        "biomarkers": "No actionable mutation found, smoker history",
        "history": "Heavily pretreated, ECOG performance status 2, life expectancy estimated under 3 months.",
    },
]


def get_all_patients():
    return PATIENTS


def get_patient_text(patient: dict) -> str:
    """Builds a single text blob from a patient's profile, used for embedding."""
    return (
        f"Diagnosis: {patient['diagnosis']}. Stage: {patient['stage_or_substage']}. "
        f"Biomarkers: {patient['biomarkers']}. History: {patient['history']}"
    )
