import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="QAInsight AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎓 QAInsight AI")

st.subheader(
    "From Quality Indicators to Insightful, Impact-Driven Decisions"
)

st.markdown("---")

# --------------------------------------------------
# INTRODUCTION
# --------------------------------------------------

st.markdown("""
## Welcome

QAInsight AI is an Artificial Intelligence-powered Decision Support System
designed for Institutional Planning, Institutional Research and
Quality Assurance in Higher Education.

---

### Demonstration Dashboards

📊 Executive Dashboard

📚 Teaching & Learning

🎓 Student Success

💬 Student Voice

🧠 Epistemic Access

📈 Strategic KPIs

🤖 AI Decision Support

---

### Purpose

This application demonstrates how strategic institutional data and AI can support:

- Evidence-based decision making
- Institutional Planning
- Quality Assurance
- Programme Review
- Student Success
- Continuous Improvement

---

### About this Demonstration

This application uses **simulated institutional data**
based on a South African university.

It is designed for demonstration purposes only.
""")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("QAInsight AI")

st.sidebar.success(
    "Select a dashboard from the navigation menu."
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "SAAIR 2026 | AI-powered Quality Assurance Decision Support System"
)
