import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------------------------
# LOAD DATA
# -----------------------------------------------------

df = pd.read_csv("data/students.csv")

# -----------------------------------------------------
# CALCULATE KPIs
# -----------------------------------------------------

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

average_satisfaction = round(
    df["Satisfaction"].mean(),
    1
)

average_epistemic = round(
    df["EpistemicAccess"].mean(),
    1
)

high_risk = len(
    df[df["RiskLevel"] == "High"]
)

# -----------------------------------------------------
# TITLE
# -----------------------------------------------------

st.title("📊 Executive Quality Assurance Dashboard")

st.write(
    "Institutional overview using simulated SMU data."
)

st.divider()

# -----------------------------------------------------
# KPI CARDS
# -----------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Students",
    total_students
)

col2.metric(
    "Pass Rate",
    f"{pass_rate}%"
)

col3.metric(
    "High Risk Students",
    high_risk
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "Average Mark",
    f"{average_mark}%"
)

col5.metric(
    "Attendance",
    f"{average_attendance}%"
)

col6.metric(
    "Epistemic Access",
    f"{average_epistemic}/100"
)

st.divider()

# -----------------------------------------------------
# SCHOOL SUMMARY
# -----------------------------------------------------

st.subheader("School Performance")

school_summary = (
    df.groupby("School")
      .agg(
          Students=("StudentID", "count"),
          AverageMark=("AssessmentAverage", "mean"),
          Attendance=("Attendance", "mean"),
          Satisfaction=("Satisfaction", "mean"),
          EpistemicAccess=("EpistemicAccess", "mean")
      )
      .round(1)
)

st.dataframe(
    school_summary,
    use_container_width=True
)

# -----------------------------------------------------
# PASS RATE BY SCHOOL
# -----------------------------------------------------

st.subheader("Average Marks by School")

fig = px.bar(
    school_summary.reset_index(),
    x="School",
    y="AverageMark",
    text_auto=".1f",
    title="Average Assessment Marks"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------------------------------
# RISK DISTRIBUTION
# -----------------------------------------------------

st.subheader("Student Risk Distribution")

risk = df["RiskLevel"].value_counts()

fig2 = px.pie(
    names=risk.index,
    values=risk.values,
    title="Risk Levels"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------------------------------------
# STUDENT VOICE
# -----------------------------------------------------

st.subheader("Student Voice")

st.dataframe(
    df[
        [
            "StudentID",
            "School",
            "Programme",
            "Comment"
        ]
    ],
    use_container_width=True
)

# -----------------------------------------------------
# AI INSIGHTS
# -----------------------------------------------------

st.divider()

st.subheader("AI Executive Insights")

if st.button("Generate Insights"):

    st.success("Analysis Complete")

    st.markdown(f"""
### Institutional Summary

**Total Students:** {total_students}

**Pass Rate:** {pass_rate}%

**Average Assessment Mark:** {average_mark}%

**Average Attendance:** {average_attendance}%

**Average Satisfaction:** {average_satisfaction}/5

**Epistemic Access Index:** {average_epistemic}/100

**High Risk Students:** {high_risk}

---

### Suggested Quality Enhancement Actions

✅ Improve assessment turnaround.

✅ Expand tutoring programmes.

✅ Increase LMS engagement.

✅ Monitor high-risk students weekly.

✅ Use student voice to guide programme improvement.

✅ Strengthen epistemic access initiatives.

""")
