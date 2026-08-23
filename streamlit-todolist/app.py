"""A simple project to-do list built with Streamlit.

Concepts this app demonstrates (useful as a teaching checklist):
  1. Streamlit's rerun model -- the whole script re-runs top-to-bottom on
     every interaction (button click, text input, etc).
  2. st.session_state -- how a Streamlit app remembers things across reruns.
  3. Reading/writing a simple JSON file for persistence (survives closing
     the browser tab or restarting the app).
  4. Basic widgets: text_input, button, checkbox, selectbox, columns.

Run it with:  streamlit run app.py
"""
import json
import os
from datetime import date

import streamlit as st

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")
PRIORITIES = ["Low", "Medium", "High"]


def load_todos():
    """Read the todo list from disk. Returns an empty list if the file
    doesn't exist yet (e.g. first run)."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    """Write the current todo list back to disk as JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


# st.session_state persists data across reruns *within one browser session*.
# We load from disk only once (the "if" guard), then keep working with the
# in-memory copy in session_state, saving to disk after every change.
if "todos" not in st.session_state:
    st.session_state.todos = load_todos()

st.set_page_config(page_title="Project To-Do List", page_icon="✅")
st.title("✅ Project To-Do List")
st.caption("A minimal Streamlit app: add, complete, and remove tasks.")

# ---- add a new task ----
with st.form("add_task_form", clear_on_submit=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        title = st.text_input("New task", placeholder="e.g. Write the intro section")
    with col2:
        priority = st.selectbox("Priority", PRIORITIES, index=1)
    submitted = st.form_submit_button("Add task")

    if submitted and title.strip():
        st.session_state.todos.append({
            "title": title.strip(),
            "priority": priority,
            "done": False,
            "created": str(date.today()),
        })
        save_todos(st.session_state.todos)

st.divider()

# ---- filters ----
show_completed = st.checkbox("Show completed tasks", value=True)

# ---- task list ----
todos = st.session_state.todos
visible = [t for t in todos if show_completed or not t["done"]]

if not visible:
    st.info("No tasks yet -- add one above to get started.")

# Iterate with the *original* index so we can safely mutate/delete the
# right item in st.session_state.todos when a button is clicked.
for i, task in enumerate(todos):
    if task not in visible:
        continue

    col_check, col_title, col_priority, col_delete = st.columns([0.5, 3, 1, 0.5])

    with col_check:
        done = st.checkbox("", value=task["done"], key=f"done_{i}")
        if done != task["done"]:
            st.session_state.todos[i]["done"] = done
            save_todos(st.session_state.todos)
            st.rerun()

    with col_title:
        label = f"~~{task['title']}~~" if task["done"] else task["title"]
        st.markdown(label)

    with col_priority:
        st.write(task["priority"])

    with col_delete:
        if st.button("🗑️", key=f"delete_{i}"):
            st.session_state.todos.pop(i)
            save_todos(st.session_state.todos)
            st.rerun()

st.divider()
done_count = sum(1 for t in todos if t["done"])
st.caption(f"{done_count}/{len(todos)} tasks completed")
