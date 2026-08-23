# Project To-Do List

A minimal, beginner-friendly to-do list app built with [Streamlit](https://streamlit.io) —
add tasks, mark them done, delete them, all in a single Python file, persisted
to a local JSON file.

Built as a teaching project — see **`Project_ToDo_List_Mentoring_Guide.pdf`**
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
- `generate_pdf.py` — regenerates the mentoring guide PDF
- `Project_ToDo_List_Mentoring_Guide.pdf` — the guide

## Author

Meharuniza
