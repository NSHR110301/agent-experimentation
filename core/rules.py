import streamlit as st

from core.engine import classify_email

st.set_page_config(layout="wide")

# Initialize rules in session
if "rules" not in st.session_state:
    st.session_state.rules = {
        "Interview": ["interview", "coding round", "assessment"],
        "Deadline": ["deadline", "submit", "last date", "due"],
        "FYI": ["newsletter", "update", "announcement", "news"],
    }

rules = st.session_state.rules
