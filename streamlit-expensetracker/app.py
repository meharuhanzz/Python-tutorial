"""A simple personal expense tracker built with Streamlit.

Concepts this app demonstrates (useful as a teaching checklist):
  1. Streamlit's rerun model -- the whole script re-runs top-to-bottom on
     every interaction (button click, text input, etc).
  2. st.session_state -- how a Streamlit app remembers things across reruns.
  3. Reading/writing a simple JSON file for persistence (survives closing
     the browser tab or restarting the app).
  4. Basic widgets: number_input, date_input, selectbox, text_input, columns.
  5. Simple data summarising: totals, grouping by category, a bar chart.

Run it with:  streamlit run app.py
"""
import json
import os
from datetime import date

import streamlit as st

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")
CATEGORIES = ["Food", "Transport", "Housing", "Utilities", "Entertainment", "Health", "Shopping", "Other"]


def load_expenses():
    """Read the expense list from disk. Returns an empty list if the file
    doesn't exist yet (e.g. first run)."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_expenses(expenses):
    """Write the current expense list back to disk as JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)


# st.session_state persists data across reruns *within one browser session*.
# We load from disk only once (the "if" guard), then keep working with the
# in-memory copy in session_state, saving to disk after every change.
if "expenses" not in st.session_state:
    st.session_state.expenses = load_expenses()

st.set_page_config(page_title="Expense Tracker", page_icon="💰")
st.title("💰 Expense Tracker")
st.caption("A minimal Streamlit app: log expenses, filter them, and see where the money goes.")

# ---- add a new expense ----
with st.form("add_expense_form", clear_on_submit=True):
    col1, col2, col3 = st.columns([1.2, 1.5, 1])
    with col1:
        amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0, format="%.2f")
    with col2:
        category = st.selectbox("Category", CATEGORIES)
    with col3:
        expense_date = st.date_input("Date", value=date.today())
    note = st.text_input("Note", placeholder="e.g. Groceries for the week")
    submitted = st.form_submit_button("Add expense")

    if submitted and amount > 0:
        st.session_state.expenses.append({
            "amount": amount,
            "category": category,
            "date": str(expense_date),
            "note": note.strip(),
        })
        save_expenses(st.session_state.expenses)

st.divider()

# ---- filter ----
filter_category = st.selectbox("Filter by category", ["All"] + CATEGORIES)

# ---- expense list ----
expenses = st.session_state.expenses
visible = [e for e in expenses if filter_category == "All" or e["category"] == filter_category]

if not visible:
    st.info("No expenses yet -- add one above to get started.")

# Iterate with the *original* index so we can safely delete the right item
# in st.session_state.expenses when a button is clicked.
for i, expense in enumerate(expenses):
    if expense not in visible:
        continue

    col_date, col_category, col_note, col_amount, col_delete = st.columns([1, 1.2, 2, 1, 0.5])

    with col_date:
        st.write(expense["date"])
    with col_category:
        st.write(expense["category"])
    with col_note:
        st.write(expense["note"] or "—")
    with col_amount:
        st.write(f"₹{expense['amount']:.2f}")
    with col_delete:
        if st.button("🗑️", key=f"delete_{i}"):
            st.session_state.expenses.pop(i)
            save_expenses(st.session_state.expenses)
            st.rerun()

st.divider()

# ---- summary ----
total = sum(e["amount"] for e in expenses)
st.metric("Total spent", f"₹{total:.2f}")

if expenses:
    by_category = {}
    for e in expenses:
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]
    st.bar_chart(by_category)
