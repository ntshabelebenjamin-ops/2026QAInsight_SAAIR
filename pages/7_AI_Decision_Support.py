import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Decision Support",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Decision Support")

st.write(
    "This dashboard demonstrates how AI can assist Quality Assurance practitioners by transforming institutional data into actionable recommendations."
)

# -------------------------
# Load Data
# -------------------------
students = pd.read_csv("data/students.csv")
modules = pd.read_csv("data/modules.csv")
kpis = pd.read_csv("data/strategic_kpis.csv")

# -------------------------
# Generate Insights
# -------------------------
if st.button("Generate Executive Insights"):

    st.subheader("Executive Summary")

    # Lowest pass rate module
    lowest_module = modules.loc[modules["PassRate"].idxmin()]

    # Red KPIs
    red = kpis[kpis["Status"] == "Red"]

    st.success("AI Analysis Completed")

    st.markdown("### Teaching & Learning")

    st.write(
        f"""
• **{lowest_module['ModuleName']}** has the lowest pass rate
(**{lowest_module['PassRate']}%**).

Recommendation:

- Review assessment design.
- Increase tutoring.
- Monitor student progression.
"""
    )

    st.markdown("### Strategic Performance")

    if len(red) == 0:

        st.write("No Red KPIs detected.")

    else:

        for _, row in red.iterrows():

            st.warning(
                f"""
**{row['KPI']}**

Target: {row['Target']}

Actual: {row['Actual']}

Responsible Office:
{row['ResponsibleOffice']}
"""
            )

    st.markdown("### Overall Recommendation")

    st.info(
        """
Priority areas requiring management attention:

• Assessment turnaround

• Student success

• Infrastructure

• Digital transformation

• Continuous monitoring of strategic KPIs

The institution should prioritise interventions in areas with declining
student outcomes and underperforming strategic indicators.
"""
    )
