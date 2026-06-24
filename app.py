"""
AI Interview Agent Pro
Main Streamlit Application
"""

import streamlit as st

from database.db import db

from pages.home import show_home
from pages.interview import show_interview
from pages.dashboard import show_dashboard
from pages.history import show_history


# ----------------------------------
# Streamlit Configuration
# ----------------------------------

st.set_page_config(
    page_title="AI Interview Agent Pro",
    page_icon="🎯",
    layout="wide"
)

# ----------------------------------
# Initialize Database
# ----------------------------------

db.create_database()

# ----------------------------------
# Sidebar
# ----------------------------------

st.sidebar.title("🎯 AI Interview Agent Pro")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Interview",
        "Dashboard",
        "History"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Open Source AI Interview Platform

    Features:
    - Answer Generation
    - Evaluation Engine
    - Dashboard Analytics
    - Interview History
    """
)

# ----------------------------------
# Page Routing
# ----------------------------------

if page == "Home":
    show_home()

elif page == "Interview":
    show_interview()

elif page == "Dashboard":
    show_dashboard()

elif page == "History":
    show_history()

# ----------------------------------
# Footer
# ----------------------------------

st.markdown("---")

st.caption(
    "AI Interview Agent Pro | MCA Final Year Project"
)
