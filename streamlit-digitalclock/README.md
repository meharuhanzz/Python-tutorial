# Digital Clock

A minimal, beginner-friendly digital clock built with [Streamlit](https://streamlit.io) —
a live, ticking clock (via embedded HTML/JS), a server-side timezone lookup
using the standard-library `zoneinfo` module, and a session-state-driven
stopwatch.

Built as a teaching project — see **`Digital_Clock_Mentoring_Guide.pdf`**
for a full walkthrough: why Streamlit needs `st.iframe` for anything that
ticks on its own, `st.session_state`, a section-by-section code
explanation, and a set of progressively harder exercises to extend the
app yourself.

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
- `Digital_Clock_Mentoring_Guide.pdf` — the guide
- `build_guide.py` — regenerates the guide PDF from its source text (run `python3 build_guide.py` after editing it)

## Author

Meharuniza
