# Plagiarism Checker

A minimal, beginner-friendly text-similarity checker built with
[Streamlit](https://streamlit.io) — paste two texts, get a similarity
score from two different comparison methods, and see exactly which
passages overlap, highlighted. No machine learning, no external API —
just the standard-library `difflib` module.

**This is a teaching tool, not a research-grade plagiarism detector.** It
only catches near-identical wording. See
**`Plagiarism_Checker_Mentoring_Guide.pdf`** for a full walkthrough of how
it works, why that limitation exists, and what a real system would need
on top of this — plus a section-by-section code explanation and a set of
progressively harder exercises to extend the app yourself.

## Run it

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run app.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`).

## Files

- `app.py` — the app
- `requirements.txt` — dependencies
- `Plagiarism_Checker_Mentoring_Guide.pdf` — the guide
- `build_guide.py` — regenerates the guide PDF from its source text (run `python3 build_guide.py` after editing it)

## Author

Meharuniza
