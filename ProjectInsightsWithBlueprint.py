import streamlit as st
import pandas as pd
import plotly.express as px

# Set page layout
st.set_page_config(layout="wide")

# Sidebar for project insights navigation
st.sidebar.title("Project Insights")
menu_options = ["RFIs", "Submittals", "Punch Items", "Observations", "Inspections", "Schedule", "Budget"]
menu_selection = st.sidebar.radio("Select Insights:", menu_options)

# Main content
st.title("Project Dashboard")

# Blueprint display with general information (mocked here)
st.subheader("Blueprint and General Information")

# Create columns for layout
col1, col2 = st.columns([2, 1])

# Display the blueprint image on the left column (mock image placeholder)
col1.image("https://via.placeholder.com/600x400", caption="A111: FIRST FLOOR - DIMENSION PLAN")

# General Information panel on the right column
with col2:
    st.write("**General Information**")
    st.write("**Number**: A111")
    st.write("**Revision**: 2")
    st.write("**Title**: FIRST FLOOR - DIMENSION PLAN")
    st.write("**Drawing Set**: ASI #6")
    st.write("**Discipline**: Architectural")
    st.write("**Set Date**: 9/7/2018")
    st.write("**Drawing Date**: 9/7/2018")
    st.write("**Received Date**: 9/10/2018")
    st.write("**Author**: Juan Engineer")
    st.button("Go to Info Page")

# Create space between sections
st.markdown("---")

# Project Insights Section
st.subheader("Project Insights Overview")

# Mock Data for the Project Insights Overview
data = {
    "Category": ["Observations", "Inspections", "Schedule", "Budget"],
    "Status": ["Open", "Closed", "Complete", "Over Budget"],
    "Count": [288, 150, 48, 15],
    "Pass Rate": ["96.20%", "90%", "48%", "29%"]
}

df = pd.DataFrame(data)

# Use columns for structured layout
insight_col1, insight_col2 = st.columns(2)

# Display insights with their statuses in the first column
with insight_col1:
    st.write("**Observations**")
    st.write(f"Status: {df.iloc[0]['Status']}")
    st.write(f"Count: {df.iloc[0]['Count']}")
    st.write(f"Pass Rate: {df.iloc[0]['Pass Rate']}")
    
    st.write("**Inspections**")
    st.write(f"Status: {df.iloc[1]['Status']}")
    st.write(f"Count: {df.iloc[1]['Count']}")
    st.write(f"Pass Rate: {df.iloc[1]['Pass Rate']}")

# Display Schedule and Budget in the second column
with insight_col2:
    st.write("**Schedule**")
    st.write(f"Status: {df.iloc[2]['Status']}")
    st.write(f"Completion: {df.iloc[2]['Pass Rate']}")
    
    st.write("**Budget**")
    st.write(f"Status: {df.iloc[3]['Status']}")
    st.write(f"Count: {df.iloc[3]['Count']}")
    st.write(f"Completion: {df.iloc[3]['Pass Rate']}")

# Budget Analysis (mocked data for visual)
budget_col1, budget_col2 = st.columns(2)

with budget_col1:
    st.write("**Revised Budget**: 949M")
    st.write("**% Complete by Cost**: 48%")
    st.write("**Job to Date Costs**: 115M")

with budget_col2:
    st.write("**Current Variance**: 29%")
    st.write("**Projected Over Under**: -840M")
