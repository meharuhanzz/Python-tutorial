"""Generates Expense_Tracker_Mentoring_Guide.pdf from this file's content
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

OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Expense_Tracker_Mentoring_Guide.pdf")

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
h1("Expense Tracker -- Mentoring Guide")
body("A Streamlit project that logs expenses, filters and deletes them, and "
     "summarises spending. This guide walks through how the app works, "
     "section by section, and closes with exercises to extend it yourself.")

# ---------------------------------------------------------- 1. rerun model
h2("1. Streamlit's rerun model")
body("Streamlit apps are not event-driven the way a desktop GUI is. There are "
     "no callback functions wired to individual clicks that run in isolation. "
     "Instead, <b>the entire script runs top to bottom every time something "
     "changes</b> -- a button click, typing in a text box, changing a "
     "selectbox. Streamlit calls this a \"rerun\".")
body("This is why the app is written as one flat script rather than a class "
     "with methods: on every rerun, every line from <font face='Courier'>import "
     "json</font> at the top down to the final <font face='Courier'>st.bar_chart</font> "
     "call runs again, in order.")
body("The practical consequence: any Python variable declared with a plain "
     "<font face='Courier'>=</font> is thrown away and recreated from scratch "
     "on every rerun. If you want something to survive across reruns -- like "
     "the list of expenses the user has entered -- you cannot just keep it in "
     "a normal variable. That's what Section 2 is for.")

# ---------------------------------------------------------- 2. session_state
h2("2. st.session_state")
body("<font face='Courier'>st.session_state</font> is a dict-like object that "
     "Streamlit keeps alive across reruns, for as long as one browser tab "
     "stays connected to the app. The app uses it for exactly one thing: "
     "holding the in-memory list of expense dictionaries.")
code(
"""if "expenses" not in st.session_state:
    st.session_state.expenses = load_expenses()"""
)
body("That guard is the key idiom. It reads the saved expenses from disk "
     "<i>once</i> -- the first time the app starts for this session -- and "
     "from then on, every rerun sees the same list already sitting in "
     "<font face='Courier'>st.session_state.expenses</font> without re-reading "
     "the file. Every place that adds or deletes an expense mutates this same "
     "list and then calls <font face='Courier'>save_expenses()</font> to write "
     "it back to disk, so the JSON file and the in-memory list never drift "
     "apart.")

# ---------------------------------------------------------- 3. persistence
h2("3. Reading and writing the JSON file")
code(
"""def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)"""
)
body("Each expense is a plain dict: <font face='Courier'>amount</font>, "
     "<font face='Courier'>category</font>, <font face='Courier'>date</font> "
     "(stored as a string, since JSON has no native date type), and "
     "<font face='Courier'>note</font>. <font face='Courier'>expenses.json</font> "
     "is just a JSON array of these dicts -- open it in a text editor after "
     "running the app once to see it for yourself.")

# ---------------------------------------------------------- 4. adding
h2("4. Adding an expense: st.form")
body("The add-expense widgets are wrapped in <font face='Courier'>with "
     "st.form(\"add_expense_form\", clear_on_submit=True):</font>. Without a "
     "form, every widget change (typing a character, moving a selectbox) "
     "triggers its own rerun immediately -- fine for a checkbox, but annoying "
     "for a multi-field entry like this one, where you want to fill in "
     "amount, category, date <i>and</i> note before anything happens. A form "
     "batches all of that: nothing is submitted until "
     "<font face='Courier'>st.form_submit_button(\"Add expense\")</font> is "
     "clicked, and <font face='Courier'>clear_on_submit=True</font> empties "
     "the fields afterwards so the form is ready for the next entry.")
code(
"""if submitted and amount > 0:
    st.session_state.expenses.append({
        "amount": amount,
        "category": category,
        "date": str(expense_date),
        "note": note.strip(),
    })
    save_expenses(st.session_state.expenses)"""
)
body("The <font face='Courier'>amount &gt; 0</font> check is a small guard "
     "against accidentally submitting an empty/zero entry -- worth noticing "
     "as a pattern: validate right before you commit data, not scattered "
     "throughout the widget code above it.")

# ---------------------------------------------------------- 5. filter+list
h2("5. Filtering and listing")
body("The category filter is an ordinary <font face='Courier'>st.selectbox</font> "
     "with <font face='Courier'>\"All\"</font> prepended to the category list. "
     "Filtering itself is a one-line list comprehension against the full "
     "<font face='Courier'>expenses</font> list -- nothing is deleted or "
     "hidden in <font face='Courier'>session_state</font>, only the on-screen "
     "<font face='Courier'>visible</font> list changes.")
body("The list is then rendered by looping over <font face='Courier'>enumerate(expenses)</font> "
     "-- the <i>full</i> un-filtered list -- and skipping rows not in "
     "<font face='Courier'>visible</font>. This matters: the loop index "
     "<font face='Courier'>i</font> is used as the delete button's "
     "<font face='Courier'>key</font> and to index into "
     "<font face='Courier'>st.session_state.expenses</font> when deleting, so "
     "it has to be the index into the <i>real</i> list, not into the filtered "
     "one -- looping over <font face='Courier'>visible</font> directly would "
     "delete the wrong row whenever a filter is active.")

# ---------------------------------------------------------- 6. delete
h2("6. Deleting: st.rerun()")
code(
"""if st.button("\U0001f5d1️", key=f"delete_{i}"):
    st.session_state.expenses.pop(i)
    save_expenses(st.session_state.expenses)
    st.rerun()"""
)
body("Every delete button needs a unique <font face='Courier'>key</font> "
     "(here, <font face='Courier'>f\"delete_{i}\"</font>) -- otherwise "
     "Streamlit can't tell which of several identical-looking buttons was "
     "clicked. After popping the item and saving, <font face='Courier'>st.rerun()</font> "
     "immediately restarts the script from the top, so the deleted row "
     "disappears from the screen right away instead of waiting for the next "
     "natural rerun.")

# ---------------------------------------------------------- 7. summary
h2("7. Summarising: st.metric and st.bar_chart")
body("The total is a one-line <font face='Courier'>sum()</font> over a "
     "generator expression, shown with <font face='Courier'>st.metric</font>. "
     "The category breakdown builds a plain dict, "
     "<font face='Courier'>{category: total_spent}</font>, by hand with a "
     "small loop -- and hands that dict straight to "
     "<font face='Courier'>st.bar_chart()</font>, which knows how to turn a "
     "dict, list, or DataFrame into a chart without any extra plotting code.")

# ---------------------------------------------------------- 8. exercises
h2("8. Exercises")
bullets([
    "<b>Edit in place.</b> Add an \"Edit\" button next to each row that lets "
    "you change the amount/category/note of an existing expense instead of "
    "deleting and re-adding it.",
    "<b>Date-range filter.</b> Add a second filter (alongside the category "
    "one) using two <font face='Courier'>st.date_input</font> widgets for a "
    "start and end date, and only show expenses in that range.",
    "<b>Monthly totals.</b> Group expenses by month (from the "
    "<font face='Courier'>date</font> string) and show a second bar chart of "
    "total spend per month.",
    "<b>Budget warning.</b> Let the user set a monthly budget with "
    "<font face='Courier'>st.number_input</font>, and show "
    "<font face='Courier'>st.warning()</font> if the current month's total "
    "goes over it.",
    "<b>CSV export.</b> Add a <font face='Courier'>st.download_button</font> "
    "that lets the user download all expenses as a CSV file (hint: build the "
    "CSV text yourself with the <font face='Courier'>csv</font> module, or "
    "just join strings by hand -- no new dependency needed).",
    "<b>Multiple currencies.</b> Add a currency selectbox per expense and "
    "make the total handle a mix of currencies sensibly (e.g. show one total "
    "per currency instead of summing them together).",
])

story.append(Spacer(1, 0.6 * cm))
body("<i>Written as a teaching companion to app.py -- read this guide with "
     "the code open side by side.</i>")

doc = SimpleDocTemplate(
    OUT_FILE, pagesize=A4,
    leftMargin=2.2 * cm, rightMargin=2.2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
    title="Expense Tracker -- Mentoring Guide",
)
doc.build(story)
print("Wrote", OUT_FILE)
