"""One-off script that builds the mentoring PDF for this project.
Run with: .venv/bin/python3 generate_pdf.py
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem,
    Preformatted, Table, TableStyle, PageBreak,
)

OUT = "Project_ToDo_List_Mentoring_Guide.pdf"

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleBig", parent=styles["Title"], fontSize=22, spaceAfter=6)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=15, spaceBefore=16, spaceAfter=8,
                     textColor=colors.HexColor("#2c4c34"))
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12, spaceBefore=10, spaceAfter=4,
                     textColor=colors.HexColor("#3f6b4a"))
body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=10.5, leading=15, spaceAfter=6)
code_style = ParagraphStyle("Code", fontName="Courier", fontSize=8.5, leading=11,
                             backColor=colors.HexColor("#f4f3ee"), borderPadding=6)

doc = SimpleDocTemplate(OUT, pagesize=A4,
                         topMargin=2*cm, bottomMargin=2*cm,
                         leftMargin=2*cm, rightMargin=2*cm)

story = []

# ---- Title page ----
story.append(Spacer(1, 3*cm))
story.append(Paragraph("Project To-Do List", title_style))
story.append(Paragraph("A Beginner-Friendly Streamlit Project", styles["Heading2"]))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph(
    "A mentoring guide: what the project is, the ideas it teaches, "
    "how the code works, and exercises to extend it yourself.",
    body))
story.append(PageBreak())

# ---- 1. Overview ----
story.append(Paragraph("1. What You're Building", h1))
story.append(Paragraph(
    "A simple to-do list web app: add tasks, mark them done, delete them, and see your "
    "progress -- all running in the browser, built entirely in Python using a framework "
    "called <b>Streamlit</b>. No HTML, CSS, or JavaScript required.",
    body))
story.append(Paragraph(
    "The tasks are saved to a small JSON file on disk, so if you close the browser tab "
    "and come back later, your list is still there.",
    body))

# ---- 2. What is Streamlit ----
story.append(Paragraph("2. What Is Streamlit, and Why Is It Different?", h1))
story.append(Paragraph(
    "Most web apps you've used follow a request/response model: the browser asks the "
    "server for something, the server sends back an answer, and nothing changes until "
    "the next request. Streamlit works differently, and this is the single most "
    "important idea to understand before reading the code:",
    body))
story.append(Paragraph(
    "<b>Every time you interact with a Streamlit app -- click a button, type in a text "
    "box, tick a checkbox -- Streamlit re-runs your <i>entire</i> Python script from top "
    "to bottom.</b> The whole file, every single time.",
    body))
story.append(Paragraph(
    "This sounds wasteful, but it's what makes Streamlit so simple to write: you just "
    "describe what the page should look like *right now*, given the current data, and "
    "Streamlit figures out how to redraw it. There's no separate step where you manually "
    "update parts of the page -- you just write normal top-to-bottom Python.",
    body))
story.append(Paragraph(
    "The catch: if the whole script re-runs constantly, how does the app remember "
    "anything (like the list of tasks) between reruns? That's what "
    "<font face='Courier'>st.session_state</font> is for -- covered in section 4.",
    body))

# ---- 3. Project structure ----
story.append(Paragraph("3. Project Structure", h1))
story.append(Preformatted(
    "meharu-todolist/\n"
    "  app.py              <- the whole app lives in this one file\n"
    "  requirements.txt     <- Python packages needed (streamlit, reportlab)\n"
    "  todos.json            <- created automatically -- your saved tasks\n"
    "  .venv/                <- virtual environment (isolated Python packages)",
    code_style))
story.append(Paragraph(
    "Keeping everything in one file is a deliberate choice for a first project -- once "
    "you're comfortable with how it works, splitting it into multiple files "
    "(e.g. a separate storage.py) is a natural next step (see the exercises).",
    body))

# ---- 4. Code walkthrough ----
story.append(Paragraph("4. Code Walkthrough", h1))

story.append(Paragraph("4.1 Loading and saving data", h2))
story.append(Paragraph(
    "Two small functions handle everything to do with the file on disk:",
    body))
story.append(Preformatted(
    "def load_todos():\n"
    "    if not os.path.exists(DATA_FILE):\n"
    "        return []\n"
    "    with open(DATA_FILE) as f:\n"
    "        return json.load(f)\n\n"
    "def save_todos(todos):\n"
    "    with open(DATA_FILE, 'w') as f:\n"
    "        json.dump(todos, f, indent=2)",
    code_style))
story.append(Paragraph(
    "Each task is just a Python dictionary: "
    "<font face='Courier'>{'title': ..., 'priority': ..., 'done': False, 'created': ...}</font>. "
    "The whole list of tasks is a list of these dictionaries, which JSON can store directly.",
    body))

story.append(Paragraph("4.2 Remembering things across reruns: st.session_state", h2))
story.append(Paragraph(
    "Since the script re-runs on every click, a plain Python variable like "
    "<font face='Courier'>todos = []</font> would reset to empty every single time. "
    "<font face='Courier'>st.session_state</font> is a dictionary-like object that "
    "Streamlit keeps alive for you across reruns, for as long as the browser tab stays open:",
    body))
story.append(Preformatted(
    "if 'todos' not in st.session_state:\n"
    "    st.session_state.todos = load_todos()   # only runs on the very first load",
    code_style))
story.append(Paragraph(
    "After this line, the rest of the script can read and modify "
    "<font face='Courier'>st.session_state.todos</font> freely, and it'll still be there "
    "on the next rerun.",
    body))

story.append(Paragraph("4.3 The add-task form", h2))
story.append(Paragraph(
    "A <font face='Courier'>st.form(...)</font> groups the text input, the priority "
    "dropdown, and the submit button together, so the app only reacts once (when "
    "'Add task' is clicked) rather than on every keystroke:",
    body))
story.append(Preformatted(
    "with st.form('add_task_form', clear_on_submit=True):\n"
    "    title = st.text_input('New task')\n"
    "    priority = st.selectbox('Priority', PRIORITIES)\n"
    "    submitted = st.form_submit_button('Add task')\n\n"
    "    if submitted and title.strip():\n"
    "        st.session_state.todos.append({...})\n"
    "        save_todos(st.session_state.todos)",
    code_style))

story.append(Paragraph("4.4 Displaying and editing the list", h2))
story.append(Paragraph(
    "The app loops over every task and draws a row of widgets for it: a checkbox, the "
    "title, the priority, and a delete button. Each widget needs a unique "
    "<font face='Courier'>key=</font> (built from the task's index, e.g. "
    "<font face='Courier'>f'done_{i}'</font>) so Streamlit can tell rows apart across "
    "reruns.",
    body))
story.append(Paragraph(
    "When something changes (a checkbox is ticked, a task is deleted), the code updates "
    "<font face='Courier'>st.session_state.todos</font>, saves it to disk, and calls "
    "<font face='Courier'>st.rerun()</font> to immediately redraw the page with the new "
    "state -- rather than waiting for the *next* natural rerun.",
    body))

# ---- 5. Running it ----
story.append(Paragraph("5. Running the App", h1))
story.append(Preformatted(
    "cd meharu-todolist\n"
    "python3 -m venv .venv\n"
    ".venv/bin/pip install -r requirements.txt\n"
    ".venv/bin/streamlit run app.py",
    code_style))
story.append(Paragraph(
    "Streamlit will print a local URL (usually http://localhost:8501) -- open it in a "
    "browser to use the app.",
    body))

# ---- 6. Exercises ----
story.append(Paragraph("6. Exercises -- Extend It Yourself", h1))
story.append(Paragraph(
    "Try these roughly in order -- each one builds on ideas already in the code:",
    body))
exercises = [
    "Add a \"due date\" field to each task (st.date_input) and show overdue tasks in red.",
    "Add an \"Edit\" button that lets you change a task's title in place.",
    "Sort tasks by priority (High first) instead of the order they were added.",
    "Add a search box (st.text_input) that filters the visible tasks by title.",
    "Show a simple bar chart (st.bar_chart) of how many tasks are High/Medium/Low priority.",
    "Split the file: move load_todos/save_todos into a separate storage.py and import it.",
    "Swap the JSON file for a small SQLite database (Python's built-in sqlite3 module) -- "
    "same idea, more scalable storage.",
    "Add multiple named lists (e.g. \"Work\", \"Personal\") using st.sidebar and a selectbox.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(e, body)) for e in exercises],
    bulletType="1", start=1,
))

story.append(Paragraph("7. Key Takeaways", h1))
takeaways = [
    "Streamlit re-runs the whole script on every interaction -- design around that, don't fight it.",
    "st.session_state is how an app remembers things across those reruns.",
    "Widgets need unique keys when you create several of the same kind in a loop.",
    "Persisting data is as simple as reading/writing a file -- you don't need a database to start.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(t, body)) for t in takeaways],
    bulletType="bullet",
))

doc.build(story)
print(f"Wrote {OUT}")
