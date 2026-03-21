import streamlit as st

from core.engine import classify_email
from core.rules import rules


def add_rule():
    label = st.session_state.new_label
    keywords = st.session_state.new_keywords

    if label and keywords:
        st.session_state.rules[label] = [k.strip() for k in keywords.split(",")]

        # clear inputs
        st.session_state.new_label = ""
        st.session_state.new_keywords = ""


st.title("📬 Email Auto-Labeler")

st.subheader("Test an Email")

subject = st.text_input("Subject")
body = st.text_area("Body")

if st.button("Classify"):
    label = classify_email(subject, body, rules)
    st.success(f"Label: {label}")


st.sidebar.header("⚙️ Manage rules")
if "new_label" not in st.session_state:
    st.session_state.new_label = ""

if "new_keywords" not in st.session_state:
    st.session_state.new_keywords = ""

new_label = st.sidebar.text_input("Label Name", key="new_label")
new_keywords = st.sidebar.text_input("Keywords (comma separated)", key="new_keywords")


if st.sidebar.button("Add Rule", on_click=add_rule):
    if new_label in rules:
        st.sidebar.warning("Label already exists")

    if new_label and new_keywords:
        rules[new_label] = [k.strip() for k in new_keywords.split(",")]

        st.sidebar.success(f"Added {new_label}")

        # ✅ Clear inputs
        st.session_state.new_label = ""
        st.session_state.new_keywords = ""


st.subheader("Existing rules")

st.write(rules)
