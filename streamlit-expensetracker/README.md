# Expense Tracker

A minimal, beginner-friendly expense tracker built with [Streamlit](https://streamlit.io) —
log expenses, filter them by category, delete them, and see a running total
and a spending-by-category chart, all in a single Python file, persisted
to a local JSON file.

Built as a teaching project — see **`Expense_Tracker_Mentoring_Guide.pdf`**
for a full walkthrough: how Streamlit's rerun model works, `st.session_state`,
a section-by-section code explanation, and a set of progressively harder
exercises to extend the app yourself.

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
- `Expense_Tracker_Mentoring_Guide.pdf` — the guide
- `build_guide.py` — regenerates the guide PDF from its source text (run `python3 build_guide.py` after editing it)

## Author

Meharuniza
