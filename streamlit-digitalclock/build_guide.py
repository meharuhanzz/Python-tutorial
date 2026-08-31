"""Generates Digital_Clock_Mentoring_Guide.pdf from this file's content
using reportlab. Not part of the app itself -- run once to (re)build the
guide after editing the text below.

Run it with:  python3 build_guide.py
"""
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, Preformatted
)

OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Digital_Clock_Mentoring_Guide.pdf")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="H1", fontSize=20, leading=24, spaceAfter=14, textColor=colors.HexColor("#1a1a2e")))
styles.add(ParagraphStyle(name="H2", fontSize=14, leading=18, spaceBefore=16, spaceAfter=8, textColor=colors.HexColor("#16213e")))
styles.add(ParagraphStyle(name="Body", fontSize=10.5, leading=15, spaceAfter=8))
styles.add(ParagraphStyle(name="CodeBlock", fontName="Courier", fontSize=8.5, leading=11, backColor=colors.HexColor("#f4f4f8"),
                           borderPadding=6, spaceAfter=10))

story = []


def h1(text):
    story.append(Paragraph(text, styles["H1"]))


def h2(text):
    story.append(Paragraph(text, styles["H2"]))


def body(text):
    story.append(Paragraph(text, styles["Body"]))


def code(text):
    story.append(Preformatted(text, styles["CodeBlock"]))


def bullets(items):
    story.append(ListFlowable(
        [ListItem(Paragraph(i, styles["Body"])) for i in items],
        bulletType="bullet", start="•", leftIndent=16,
    ))


# ---------------------------------------------------------------- title ----
h1("Digital Clock -- Mentoring Guide")
body("A Streamlit project with three small, self-contained pieces: a live "
     "ticking clock, a server-side timezone lookup, and a stopwatch. This "
     "guide walks through how each one works and why it's built the way it "
     "is, then closes with exercises to extend it yourself.")

# --------------------------------------------------- 1. rerun model recap
h2("1. Why a clock can't just be `st.write(datetime.now())`")
body("Streamlit's whole script re-runs top to bottom whenever something "
     "happens -- a click, a text edit, a call to <font face='Courier'>st.rerun()</font>. "
     "Nothing makes it re-run once a second on its own. If you wrote "
     "<font face='Courier'>st.write(datetime.now())</font> at the top of "
     "this app, it would print the time the page was <i>loaded</i>, and "
     "then sit there frozen until the next interaction -- not what a clock "
     "needs.")
body("That's the problem this app's first section solves.")

# --------------------------------------------------- 2. st.iframe clock
h2("2. The live clock: st.iframe")
body("<font face='Courier'>st.iframe()</font> embeds raw HTML (and any "
     "JavaScript inside it) directly into the page, in a sandboxed iframe. "
     "Unlike the rest of a Streamlit app, that JavaScript keeps running in "
     "the browser completely independently of Streamlit's rerun model -- "
     "it never talks to the Python server again after the page loads.")
code(
"""<script>
  function tick() {
    const now = new Date();
    const pad = (n) => String(n).padStart(2, "0");
    document.getElementById("clock").textContent =
      pad(now.getHours()) + ":" + pad(now.getMinutes()) + ":" + pad(now.getSeconds());
  }
  tick();
  setInterval(tick, 1000);
</script>"""
)
body("<font face='Courier'>setInterval(tick, 1000)</font> is plain "
     "JavaScript: call <font face='Courier'>tick()</font> every 1000ms. "
     "This is the only part of the whole app that updates without a "
     "Streamlit rerun -- worth noticing as the general pattern for "
     "\"anything that must animate or tick on its own\" in a Streamlit app: "
     "reach for HTML/JS via <font face='Courier'>st.iframe</font>, not "
     "Python-side polling loops.")

# --------------------------------------------------- 3. zoneinfo
h2("3. Server-side time: the zoneinfo standard-library module")
body("The second section is ordinary Python, computed fresh on every "
     "rerun. <font face='Courier'>zoneinfo</font> (standard library since "
     "Python 3.9, no <font face='Courier'>pip install</font> needed) gives "
     "<font face='Courier'>datetime</font> real timezone awareness:")
code(
"""from zoneinfo import ZoneInfo
from datetime import datetime

now_in_tz = datetime.now(ZoneInfo("Asia/Kolkata"))"""
)
body("Because this part has no JavaScript ticking it, it's only ever as "
     "fresh as the last rerun -- which is exactly why there's an explicit "
     "\"Refresh\" button next to it. This contrast (JS clock: always live; "
     "Python clock: live only when Streamlit reruns) is the single most "
     "important thing this app demonstrates about how Streamlit works.")

# --------------------------------------------------- 4. stopwatch
h2("4. The stopwatch: session_state, not a running counter")
body("A natural first instinct for a stopwatch is a loop that increments a "
     "counter once a second. That doesn't work in Streamlit -- a script "
     "that never returns blocks the whole app from handling any other "
     "interaction. Instead, this app stores <i>when</i> the stopwatch was "
     "started, and computes elapsed time from that timestamp on every "
     "rerun:")
code(
"""if st.button("▶ Start", disabled=st.session_state.stopwatch_start is not None):
    st.session_state.stopwatch_start = time.time()
    st.rerun()"""
)
body("Stopping adds the just-elapsed interval "
     "(<font face='Courier'>time.time() - stopwatch_start</font>) onto a "
     "running total, <font face='Courier'>stopwatch_elapsed</font>, and "
     "clears <font face='Courier'>stopwatch_start</font> back to "
     "<font face='Courier'>None</font>. While running, the displayed "
     "elapsed time is computed as "
     "<font face='Courier'>stopwatch_elapsed + (time.time() - stopwatch_start)</font> "
     "-- the sum of all previously-completed stop/start segments, plus "
     "whatever has ticked by since the current segment began.")
body("Every button here calls <font face='Courier'>st.rerun()</font> right "
     "after mutating state, for the same reason the to-do list and expense "
     "tracker projects do: without it, a state change made by one click "
     "only becomes visible on screen at the <i>next</i> rerun, not "
     "immediately -- try removing a <font face='Courier'>st.rerun()</font> "
     "call and clicking Start once to see the one-click lag for yourself.")
body("Each button is also individually <font face='Courier'>disabled</font> "
     "based on current state (Start disabled while running, Stop disabled "
     "while stopped) -- a small guard against double-starting or "
     "double-stopping the same stopwatch.")

# --------------------------------------------------- 5. exercises
h2("5. Exercises")
bullets([
    "<b>12-hour format toggle.</b> Add a checkbox that switches the live "
    "JS clock between 24-hour and 12-hour (AM/PM) display.",
    "<b>Lap times.</b> Add a \"Lap\" button to the stopwatch that appends "
    "the current elapsed time to a list in <font face='Courier'>session_state</font>, "
    "and display the list of laps below it (same list-in-session-state "
    "pattern the to-do list and expense tracker use).",
    "<b>Countdown timer.</b> Build a third section: let the user enter a "
    "number of seconds, and count down instead of up -- reuse the "
    "start-timestamp trick, but compute <i>remaining</i> time instead of "
    "elapsed time.",
    "<b>More timezones.</b> Replace the fixed <font face='Courier'>TIMEZONES</font> "
    "list with a searchable selectbox over all of "
    "<font face='Courier'>zoneinfo.available_timezones()</font> (hundreds "
    "of entries) instead of the six hand-picked ones.",
    "<b>World clock grid.</b> Show four or five timezones at once, side by "
    "side in columns, instead of one at a time via a selectbox.",
])

story.append(Spacer(1, 0.6 * cm))
body("<i>Written as a teaching companion to app.py -- read this guide with "
     "the code open side by side.</i>")

doc = SimpleDocTemplate(
    OUT_FILE, pagesize=A4,
    leftMargin=2.2 * cm, rightMargin=2.2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
    title="Digital Clock -- Mentoring Guide",
)
doc.build(story)
print("Wrote", OUT_FILE)
