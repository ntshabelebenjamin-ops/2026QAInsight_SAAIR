import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Teaching & Learning", page_icon="📚", layout="wide")

st.title("📚 Teaching & Learning Dashboard")
st.caption("Module Performance | Assessment Quality | Academic Monitoring")

# -------------------------
# Load Data
# -------------------------
df = pd.read_csv("data/modules.csv")

# -------------------------
# KPI Cards
# -------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Modules", len(df))
col2.metric("Average Pass Rate", f"{df['PassRate'].mean():.1f}%")
col3.metric("Average Mark", f"{df['AverageMark'].mean():.1f}%")
col4.metric("Avg Turnaround", f"{df['AssessmentTurnaroundDays'].mean():.1f} Days")

st.divider()

# -------------------------
# Module Performance
# -------------------------
st.subheader("Module Pass Rates")

fig = px.bar(
    df,
    x="ModuleCode",
    y="PassRate",
    color="School",
    text="PassRate"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Assessment Turnaround
# -------------------------
st.subheader("Assessment Turnaround")

fig2 = px.bar(
    df,
    x="ModuleCode",
    y="AssessmentTurnaroundDays",
    color="School",
    text="AssessmentTurnaroundDays"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Moderation Status
# -------------------------
st.subheader("Moderation Status")

fig3 = px.pie(
    df,
    names="ModerationStatus"
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------
# Module Table
# -------------------------
st.subheader("Module Summary")

st.dataframe(df, use_container_width=True)

# -------------------------
# AI Quality Insights
# -------------------------
st.subheader("🤖 AI Quality Insights")

lowest = df.loc[df["PassRate"].idxmin()]
slowest = df.loc[df["AssessmentTurnaroundDays"].idxmax()]

st.info(
    f"""
**Module requiring attention:** {lowest['ModuleCode']} - {lowest['ModuleName']}

• Lowest Pass Rate: **{lowest['PassRate']}%**

• Assessment Turnaround: **{lowest['AssessmentTurnaroundDays']} days**

• Moderation Status: **{lowest['ModerationStatus']}**

### Suggested Quality Actions

- Review assessment design.
- Increase tutoring and supplemental instruction.
- Improve feedback turnaround time.
- Monitor student performance during the semester.
"""
)
