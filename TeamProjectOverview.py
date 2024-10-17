import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Title for the App
st.title("Project Home")

# Project Team Section
st.subheader("Project Team")

# Create Data for the Project Team table
team_data = {
    'Role': ['Project Manager', 'Superintendent', 'Project Engineer'],
    'Name': ['Elise East (Electri-Con Services LLC)', 'Elsa Soo (Superintendent Electri-Con)', 'Eli (Project Engineer Electri-Con)'],
    'Email': ['test.electri-elise@projectmanager@icloud.com', 'test.elsa.superintendent@icloud.com', 'test.electri-eli.projectengineer@icloud.com'],
    'Office': ['', '', ''],
    'Mobile': ['', '', '']
}
df_team = pd.DataFrame(team_data)

# Display Project Team as a Table
st.table(df_team)

# Project Overview Section
st.subheader("Project Overview")

# Create data for Project Overview bar chart
categories = ['RFIs', 'Submittals', 'Schedule', 'Inspections', 'Observations', 'Punchlist', 'Meetings', 'Tasks']
overdue = [1, 2, 0, 1, 3, 1, 2, 0]
next_7_days = [2, 1, 3, 2, 0, 0, 0, 3]
over_7_days = [3, 4, 5, 3, 0, 0, 1, 5]
total_open = [6, 7, 8, 6, 3, 1, 3, 8]

# Create a bar chart with Plotly
fig = go.Figure()

# Adding traces for each category
fig.add_trace(go.Bar(
    x=categories, 
    y=overdue, 
    name='Overdue', 
    marker_color='red'
))
fig.add_trace(go.Bar(
    x=categories, 
    y=next_7_days, 
    name='Next 7 Days', 
    marker_color='yellow'
))
fig.add_trace(go.Bar(
    x=categories, 
    y=over_7_days, 
    name='>7 Days', 
    marker_color='green'
))

# Update layout for better visualization
fig.update_layout(
    barmode='stack',
    title="Project Overview",
    xaxis_title="Category",
    yaxis_title="Count",
    legend_title="Status"
)

# Display the Project Overview Chart
st.plotly_chart(fig)

# Open Items Section
st.subheader("My Open Items")

# Create data for Open Items
open_items_data = {
    'Type': ['RFI', 'Business Development'],
    'Title': ['Solar Panel Foundation', 'Water Damage - Wiring'],
    'Status': ['Draft', 'Review for Review'],
    'Due Date': ['02/01/2019', '05/04/2019']
}
df_open_items = pd.DataFrame(open_items_data)

# Display Open Items as a table
st.table(df_open_items)

# Sidebar with Project Info and Weather
st.sidebar.title("Project Information")

# Add project address
st.sidebar.write("**Project Address**")
st.sidebar.write("6307 Carpinteria Ave, Carpinteria, CA 93013, United States")

# Add Weather Info
st.sidebar.write("**Project Weather**")
st.sidebar.write("Clear")
st.sidebar.write("Temp: 71°F | Wind: 2mph")
st.sidebar.write("Humidity: 46%")

# Add date, time, etc.
st.sidebar.write("**Date**: 08/01/2019")
st.sidebar.write("**Time**: 2:54 PM")
