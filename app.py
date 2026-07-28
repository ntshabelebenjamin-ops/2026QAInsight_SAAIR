import streamlit as st

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="QAInsight AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

st.title("🎓 QAInsight AI")

st.subheader(
    "From Quality Indicators to Insightful, Impact-Driven Decisions"
)

st.markdown("---")

# ----------------------------------------------------
# INTRODUCTION
# ----------------------------------------------------

st.markdown("""
## Welcome

QAInsight AI is an Artificial Intelligence-powered Decision Support System
developed to demonstrate how Strategic Data can strengthen
Quality Assurance in Higher Education.

This demonstration is inspired by the SAAIR 2026 Quality Forum.

---

### What you can explore

📊 Executive Dashboard

📚 Teaching & Learning Analytics

🎓 Student Success Analytics

💬 Student Voice

🧠 Epistemic Access

📈 Strategic KPIs

🤖 AI Quality Insights

---

### Objectives

This platform demonstrates how Artificial Intelligence can help universities:

- Improve evidence-based decision making
- Enhance programme quality
- Monitor institutional performance
- Analyse student feedback
- Identify students at risk
- Strengthen epistemic access
- Support continuous quality improvement

---

### Institution

This application uses **simulated data** based on a South African
Higher Education Institution for demonstration purposes only.
""")

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

st.sidebar.title("QAInsight AI")

st.sidebar.success(
    "Select a dashboard from the navigation menu."
)

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown("---")

st.caption(
    "Developed for the SAAIR 2026 Quality Forum | Simulation Data Only"
)
