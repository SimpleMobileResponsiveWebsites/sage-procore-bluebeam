import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Project Gantt Chart", layout="wide")

# Custom CSS for layout
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .stButton>button {
        height: 2em;
        padding: 0rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("Project Gantt Chart")

# Action buttons
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("Refresh")
with col2:
    st.button("Back")
with col3:
    st.button("Forward")
with col4:
    st.button("Zoom In")
with col5:
    st.button("Zoom Out")

# Create sample data
data = {
    "Task": ["Project: Data Resource", "Access DE Target", "IN: Campaign Data", "Create Brief", "PH: Identify Criteria"],
    "Start": ["2023-05-01", "2023-05-01", "2023-05-05", "2023-05-10", "2023-05-15"],
    "Finish": ["2023-05-31", "2023-05-10", "2023-05-20", "2023-05-15", "2023-05-25"],
    "Status": ["In Progress", "In Progress", "In Progress", "In Progress", "In Progress"],
    "Complete %": [0, 0, 0, 0, 0],
}

df = pd.DataFrame(data)

# Display the dataframe
st.dataframe(df)

# Create Gantt chart
fig = ff.create_gantt(df, index_col="Task", show_colorbar=True, group_tasks=True)

# Update layout
fig.update_layout(
    title="Project Gantt Chart",
    xaxis_title="Date",
    yaxis_title="Task",
    height=400,
    margin=dict(l=250, r=20, t=50, b=20)
)

# Display the Gantt chart
st.plotly_chart(fig, use_container_width=True)

# Footer
st.write("Sage Intacct Inventory Automation")
st.image("https://www.sage.com/en-us/-/media/images/sagedotcom/master/logos/sage_logo_social.png", width=100)

# Video player placeholder
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Footer (placeholder for video controls)
st.write("2:45 / 3:01")
