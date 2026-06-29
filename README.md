# 🧬 AI-Powered Clinical Trial Matching System

An NLP-based tool that matches patient profiles to clinical trials using a combination of **hard eligibility filters** (age, sex, diagnosis) and **semantic similarity via sentence embeddings** (transformer-based) on the fuzzier eligibility criteria — with full explainability for every match.

---

## ⚠️ Important: read this first

This is a **portfolio/demonstration project**, not a clinical decision-making tool:
- **Patient profiles are entirely synthetic** — invented for this project, not real patient data. This is a deliberate design choice: real patient data is protected health information (PHI), and using it would raise serious privacy/compliance issues that are out of scope for a demo project.
- **Trial data is real** (sourced from ClinicalTrials.gov, see "Data provenance" below), but eligibility criteria have been condensed and restructured for this project. Always consult the official ClinicalTrials.gov record before any real-world decision.
- This tool does **not** replace a clinician, clinical research coordinator, or the official trial screening process.

## Why this problem matters

Clinical trial recruitment is one of the biggest bottlenecks in medical research — studies are frequently delayed or fail to reach enrollment targets because matching patients to relevant, eligible trials is slow and manual. This is a real job function at pharmaceutical companies, CROs (Contract Research Organizations), and academic medical centers. This project demonstrates the core technique behind real trial-matching tools: combining structured eligibility rules with semantic text matching.

## How it works

1. **Hard filters first.** Age range, sex, and diagnosis/condition match are treated as non-negotiable eligibility facts — a trial only enters the ranking pool if the patient actually qualifies on these. This mirrors how real eligibility screening works: some criteria are binary cutoffs, not similarity scores.
2. **Semantic similarity second.** Among trials that pass the hard filters, the patient's free-text history is converted into a sentence embedding (using `sentence-transformers`, model `all-MiniLM-L6-v2`) and compared against each trial's inclusion/exclusion criteria using cosine similarity. This is what lets the system match, for example, "never treated with interferon beta-1b" to a trial requiring "interferon beta-1b naive" even though the wording differs.
3. **Explainability.** For every match, the system surfaces the *single specific criterion sentence* that was most similar to the patient's profile — so a user can see exactly why a trial was suggested, instead of trusting an opaque score.

## Tech stack

- **Python** + **pandas**-style structured data (plain dicts/lists, kept simple and inspectable)
- **sentence-transformers** (`all-MiniLM-L6-v2`) for transformer-based semantic embeddings
- **NumPy** for cosine similarity calculations
- **Streamlit** for the interactive interface

## Data provenance

**Trials:** All 15 trials in `data/trials.py` are real studies from [ClinicalTrials.gov](https://clinicaltrials.gov), identified by their actual NCT ID, covering three conditions: Multiple Sclerosis, HER2-positive Breast Cancer, and Non-Small Cell Lung Cancer (NSCLC). Eligibility criteria are taken from each trial's real published record, condensed into structured fields for this project.

One note on sourcing: ClinicalTrials.gov's bulk API (`api/v2/studies`) returned errors from this build environment, so trials were sourced individually by searching and reading each study's public page rather than via a single bulk pull.

**Patients:** All 20 patient profiles in `data/patients.py` are synthetic/invented, designed to span a realistic range of ages, diagnoses, stages, and biomarker statuses relevant to the trials in the dataset (including some patients who deliberately *shouldn't* match certain trials, to test the hard-filter logic).

## Project structure

```
trial-matcher/
├── app.py                  # Streamlit application (main entry point)
├── matching.py              # Core matching engine: hard filters + semantic similarity
├── requirements.txt
├── data/
│   ├── trials.py            # Real ClinicalTrials.gov trial data
│   └── patients.py          # Synthetic patient profiles
└── README.md
```

## Running it locally

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/trial-matcher.git
cd trial-matcher

# 2. (Recommended) create a virtual environment
python3 -m venv venv
source venv/bin/activate       # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The first run will download the `all-MiniLM-L6-v2` model (~80MB) automatically from Hugging Face — this requires an internet connection the first time only; the model is cached locally afterward.

The app will open at `http://localhost:8501`.

## Possible extensions

- Add more conditions/trials to broaden coverage.
- Pull trials live from the ClinicalTrials.gov API instead of a static dataset (the API was unreachable from the build sandbox used for this project, but should work fine from most other environments).
- Add a confidence threshold slider so users can tune how strict the semantic matching is.
- Highlight overlapping keywords between patient text and trial criteria, not just the overall similarity score.
- Swap in a larger/more domain-specific embedding model (e.g. a clinical/biomedical sentence transformer) for potentially better matching on medical terminology.

## Why this project

Built as a focused demonstration of:
- NLP / semantic search using transformer-based sentence embeddings
- Healthcare/clinical research domain knowledge (eligibility criteria structure, the real-world recruitment bottleneck)
- Responsible AI design — hard rules where rules matter, semantic matching only where it adds genuine value, and explainability instead of a black-box score
- Practical, honest data sourcing (real trial data, clearly synthetic patient data, transparent about API limitations encountered)

---
*This is an educational/portfolio project and is not intended for clinical or research recruitment use.*
