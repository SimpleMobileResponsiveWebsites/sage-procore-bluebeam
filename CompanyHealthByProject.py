import streamlit as st
import pandas as pd
import numpy as np

# Function to generate progress bar with color
def progress_bar(value):
    color = '#2196F3'  # default color (blue)
    if value >= 80:
        color = '#4CAF50'  # green
    elif 50 <= value < 80:
        color = '#FFEB3B'  # yellow
    elif value < 50:
        color = '#F44336'  # red
    
    st.markdown(f"""
    <div style="width: 100%; background-color: #e0e0e0; border-radius: 4px;">
        <div style="width: {value}%; background-color: {color}; height: 10px; border-radius: 4px;"></div>
    </div>
    """, unsafe_allow_html=True)

# Project data
data = {
    'Project Health': [98, 92, 85, 67, 58, 45],
    'Project Name': ['206 Museum', '221 Chase', '816 Congress', 'Alamo Draft House', 'Austin Skyline', 'The One Toronto'],
    'Schedule': [90, 85, 80, 60, 55, 45],
    'Over/Under': [780000, 25000, -62000, 447932, 188432, -30000],
    'Submittals Past Due': [True, False, False, False, False, True],
    'RFIs Past Due': [False, False, False, True, False, False],
    'Change Orders Unapproved': [False, False, True, False, False, True]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Header
st.title("Company Health by Project")

# Display Data as a table
for index, row in df.iterrows():
    col1, col2, col3, col4, col5, col6 = st.columns([1, 3, 2, 2, 2, 2])

    # Project Health (with colored circle)
    if row['Project Health'] >= 80:
        health_color = 'green'
    elif 50 <= row['Project Health'] < 80:
        health_color = 'yellow'
    else:
        health_color = 'red'
    
    col1.markdown(f"<div style='border-radius: 50%; width: 30px; height: 30px; background-color: {health_color}; text-align: center; color: white; line-height: 30px;'>{row['Project Health']}</div>", unsafe_allow_html=True)
    
    # Project Name
    col2.write(row['Project Name'])

    # Schedule Progress Bar
    col3.write(f"{row['Schedule']}%")
    progress_bar(row['Schedule'])

    # Over/Under Budget
    col4.write(f"${row['Over/Under']:,.2f}")

    # Submittals Past Due (indicator)
    if row['Submittals Past Due']:
        col5.markdown(f"<div style='color: red;'>•</div>", unsafe_allow_html=True)
    else:
        col5.markdown(f"<div style='color: green;'>•</div>", unsafe_allow_html=True)

    # RFIs Past Due (indicator)
    if row['RFIs Past Due']:
        col6.markdown(f"<div style='color: yellow;'>•</div>", unsafe_allow_html=True)
    else:
        col6.markdown(f"<div style='color: green;'>•</div>", unsafe_allow_html=True)

    # Change Orders Unapproved (indicator)
    col7, = st.columns(1)
    if row['Change Orders Unapproved']:
        col7.markdown(f"<div style='color: red;'>•</div>", unsafe_allow_html=True)
    else:
        col7.markdown(f"<div style='color: green;'>•</div>", unsafe_allow_html=True)

# Sidebar with extra info (if needed)
st.sidebar.title("Project Information")
st.sidebar.write("Company Health by Projects Dashboard")
