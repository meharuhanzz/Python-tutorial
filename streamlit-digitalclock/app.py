"""A digital clock + stopwatch built with Streamlit.

Concepts this app demonstrates (useful as a teaching checklist):
  1. st.iframe -- embedding raw HTML/JS in a Streamlit app, and why that's
     needed for anything that must tick every second (Streamlit's rerun
     model, on its own, only updates the page when *you* interact with it
     or call st.rerun() -- it doesn't auto-refresh on a timer).
  2. The zoneinfo standard-library module -- showing the current time in
     several timezones, computed in Python.
  3. st.session_state used to build a stopwatch: storing a start timestamp
     across reruns and computing elapsed time from it, rather than trying
     to keep a "live" counter running server-side.
  4. Basic widgets: selectbox, columns, button.

Run it with:  streamlit run app.py
"""
import time
from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

import streamlit as st

TIMEZONES = ["UTC", "Asia/Kolkata", "America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney"]
TIMEZONES = [tz for tz in TIMEZONES if tz in available_timezones()]

st.set_page_config(page_title="Digital Clock", page_icon="🕒")
st.title("🕒 Digital Clock")
st.caption("A live client-side clock, server-side timezone lookups, and a session-state stopwatch.")

# ---- live clock (client-side JS -- ticks every second with no server round trip) ----
st.subheader("Live clock")
st.iframe(
    """
    <div style="font-family: 'Courier New', monospace; font-size: 3rem;
                text-align: center; padding: 0.5rem 0; color: #1a1a2e;">
      <span id="clock">--:--:--</span>
    </div>
    <script>
      function tick() {
        const now = new Date();
        const pad = (n) => String(n).padStart(2, "0");
        const el = document.getElementById("clock");
        if (el) {
          el.textContent = pad(now.getHours()) + ":" + pad(now.getMinutes()) + ":" + pad(now.getSeconds());
        }
      }
      tick();
      setInterval(tick, 1000);
    </script>
    """,
    height=90,
)
st.caption("Ticks in your browser via JavaScript -- Streamlit's own rerun model can't "
           "update a page once per second on its own without this kind of component.")

st.divider()

# ---- server-side timezone clock ----
st.subheader("Time in another timezone")
st.caption("Computed in Python with the stdlib `zoneinfo` module -- refresh to update.")

col1, col2 = st.columns([1, 1])
with col1:
    tz_name = st.selectbox("Timezone", TIMEZONES)
with col2:
    st.write("")
    st.write("")
    refresh = st.button("Refresh")

now_in_tz = datetime.now(ZoneInfo(tz_name))
st.metric(tz_name, now_in_tz.strftime("%H:%M:%S"), now_in_tz.strftime("%A, %d %B %Y"))

st.divider()

# ---- stopwatch ----
st.subheader("Stopwatch")
st.caption("Built with st.session_state: we store *when* it was started, and compute "
           "elapsed time from that on every rerun -- not a running counter.")

if "stopwatch_start" not in st.session_state:
    st.session_state.stopwatch_start = None
if "stopwatch_elapsed" not in st.session_state:
    st.session_state.stopwatch_elapsed = 0.0

col_start, col_stop, col_reset = st.columns(3)
with col_start:
    if st.button("▶ Start", disabled=st.session_state.stopwatch_start is not None):
        st.session_state.stopwatch_start = time.time()
        st.rerun()
with col_stop:
    if st.button("⏸ Stop", disabled=st.session_state.stopwatch_start is None):
        st.session_state.stopwatch_elapsed += time.time() - st.session_state.stopwatch_start
        st.session_state.stopwatch_start = None
        st.rerun()
with col_reset:
    if st.button("↺ Reset"):
        st.session_state.stopwatch_start = None
        st.session_state.stopwatch_elapsed = 0.0
        st.rerun()

if st.session_state.stopwatch_start is not None:
    current_elapsed = st.session_state.stopwatch_elapsed + (time.time() - st.session_state.stopwatch_start)
    st.info("Running -- press Refresh above or interact with the page to update the reading.")
else:
    current_elapsed = st.session_state.stopwatch_elapsed

minutes, seconds = divmod(current_elapsed, 60)
st.metric("Elapsed", f"{int(minutes):02d}:{seconds:05.2f}")
