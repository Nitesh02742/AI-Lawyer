# AI Lawyer – AI helper for consumer problems in India

A chat app where an ordinary person explains a consumer problem (refund not received, defective product,
bad service, online shopping) in Hindi, English or another Indian language, by typing or by voice.
It then:

1. **Builds the case**: turns the messy story into a timeline, proof they have, proof to collect.
2. **Explains where they stand**: options in plain language, cheapest first.
3. **Drafts a legal notice** they can send themselves.
4. **Knows its limits**: says when it is not sure and when they need a real lawyer.

## How it avoids made-up laws

- `knowledge_base.json` is a small file of **verified** facts, each with an official or reputable source link.
  Only entries with `"status": "verified"` are shown to the model.
- The model must tag every legal fact with its source, e.g. `[KB:NCH]`.
- A code **guard** (`check_answer` in `lawyer_core.py`) scans every answer for section numbers, court-case
  citations, helpline numbers and source tags that are **not** in the verified file. If it finds any, the
  model is asked once to rewrite; anything still left is shown to the user as a warning.
- The user sees the source links under each answer.

## Files

| File | What it does |
|---|---|
| `app.py` | The Streamlit chat app (text + voice, case file, legal notice, save conversation) |
| `lawyer_core.py` | Prompts, model calls, the hallucination guard. `MODEL_NAME` swaps the model |
| `knowledge_base.json` | Verified law facts with sources |
| `test_cases.json` | 12 test cases: normal, messy, Hindi/Hinglish/Tamil, out-of-scope, safety, hallucination traps |
| `run_tests.py` | Runs all test cases and saves unedited outputs to `outputs/<time>/` |

## Run on your computer

```bash
pip install -r requirements.txt
# put your key in .streamlit/secrets.toml  ->  GEMINI_API_KEY = "AIza..."
streamlit run app.py
```

Run the test cases (raw outputs):

```bash
export GEMINI_API_KEY="AIza..."        # Windows: set GEMINI_API_KEY=AIza...
python run_tests.py
```

Each run creates `outputs/<date_time>/` with a copy of `test_cases.json`, one `.json` (raw) and one `.md`
(readable) file per test case, and `summary.csv`. These files are saved unedited.

Check the guard alone (no API key needed): `python test_guard.py`

Swap the model: set `MODEL_NAME` (env variable) or type another model name in the app sidebar. If the model is
busy, out of quota or unavailable, the app retries and falls back to `gemini-3.6-flash`, then `gemini-3.5-flash-lite`.

## Deploy free on Streamlit Community Cloud

1. Push this folder to a public GitHub repo (the key is NOT in the repo; `.gitignore` excludes secrets).
2. On share.streamlit.io → **Create app** → pick the repo → main file `app.py`.
3. **Advanced settings → Secrets**: add `GEMINI_API_KEY = "AIza..."` → Deploy.

## What it covers / does not cover

Covers: consumer complaints in India (goods and services, online and offline).
Does not cover: criminal matters, landlord–tenant and property, family, salary/employment, cyber fraud,
very high-value claims. For these it tells the user to see a lawyer or the District Legal Services Authority.

This tool gives general information, not legal advice.
