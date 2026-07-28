import streamlit as st
import pandas as pd

def load_sidebar():

    st.sidebar.image(
        "https://img.icons8.com/fluency/96/graduation-cap.png",
        width=80
    )

    st.sidebar.title("QAInsight AI")

    st.sidebar.markdown("---")

    school = st.sidebar.selectbox(
        "Select School",
        [
            "All",
            "School of Medicine",
            "School of Oral Health Sciences",
            "School of Pharmacy",
            "School of Health Care Sciences",
            "School of Science and Technology"
        ]
    )

    semester = st.sidebar.selectbox(
        "Semester",
        ["All", "1", "2"]
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
QAInsight AI

Institutional Planning

Quality Assurance

Decision Support

AI Analytics
"""
    )

    return school, semester
