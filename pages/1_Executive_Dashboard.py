import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Quality Assurance Dashboard")
st.caption("Simulated Institutional Data | SAAIR 2026 Demonstration")

# -----------------------------
# Load Data
# -----------------------------
try:
    from utils.data_loader import load_students

df = load_students()
except Exception as e:
    st.error(f"Unable to load students.csv\n\n{e}")
    st.stop()

# -----------------------------
# Calculate KPIs
# -----------------------------
total_students = len(df)

pass_rate = round(
    (df["AssessmentAverage"] >= 50).mean() * 100,
    1
)

average_mark = round(
    df["AssessmentAverage"].mean(),
    1
)

average_attendance = round(
    df["Attendance"].mean(),
    1
)

high_risk = len(
    df[df["RiskLevel"] == "High"]
)

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Students", f"{total_students:,}")

col2.metric("Pass Rate", f"{pass_rate}%")

col3.metric("Average Mark", f"{average_mark}%")

col4.metric("High Risk Students", high_risk)

st.divider()

# -----------------------------
# School Summary
# -----------------------------
st.subheader("Performance by School")

school_summary = (
    df.groupby("School")
      .agg(
          Students=("StudentID", "count"),
          AverageMark=("AssessmentAverage", "mean"),
          Attendance=("Attendance", "mean")
      )
      .round(1)
)

st.dataframe(
    school_summary,
    use_container_width=True
)

# -----------------------------
# Charts
# -----------------------------
st.subheader("Average Marks by School")

fig = px.bar(
    school_summary.reset_index(),
    x="School",
    y="AverageMark",
    text_auto=".1f"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Risk Distribution")

risk = df["RiskLevel"].value_counts().reset_index()
risk.columns = ["Risk Level", "Students"]

fig2 = px.pie(
    risk,
    names="Risk Level",
    values="Students"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Student Voice
# -----------------------------
st.subheader("Recent Student Comments")

st.dataframe(
    df[
        [
            "StudentID",
            "School",
            "Comment"
        ]
    ].head(10),
    use_container_width=True
)

st.success("Executive Dashboard Loaded Successfully")
