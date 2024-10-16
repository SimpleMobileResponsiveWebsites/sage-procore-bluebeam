import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Cubit Services Financials - Project Manager", layout="wide")

# Custom CSS for layout
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .metric-container {
        background-color: white;
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
    }
    .dataframe {
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.image("https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png", width=100)
with col2:
    st.title("Cubit Services Financials")
with col3:
    st.write("CLIENT USA")
    st.write("John G")
    st.write("Help & Support")

# Navigation
st.sidebar.title("Navigation")
st.sidebar.button("Dashboards")

# Main content
st.header("Project Manager")

# Summary metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Project net profit", "$1,077,569", "+$52,265 vs prior month")
with col2:
    st.metric("Billed Revenue", "$6,311,093", "")
with col3:
    st.metric("Work in Progress", "$1,885,500", "")
with col4:
    st.metric("All Hours", "18,742", "+652 vs prior month")

# Financial Summary Table
st.subheader("My Projects Financial Summary")

financial_data = {
    "Project": ["JENTETCH Consulting", "StaffTru", "Been Verified", "Grand Financial Services", "Conductor", "Intelligent Audit"],
    "Contract Value": [5400, 218950, 272750, 136450, 235500, 276900],
    "Revenue": [5515.67, 160842.13, 207750.00, 147450.00, 128611.00, 93640.53],
    "A/R": [0.00, 65883.39, 65000.00, 0.00, 34941.32, 144016.80],
    "Billed": [5515.67, 226725.52, 272750.00, 147450.00, 163552.32, 237657.33],
    "Received": [5515.67, 160842.13, 207750.00, 147450.00, 128611.00, 93640.53],
    "Labor Costs": [769.00, 19751.28, 46318.47, 8144.17, 27190.32, 14031.91],
    "Non-Labor Costs": [1250.82, 12812.60, 15595.64, 0.00, 2781.32, 11178.40],
    "Total Costs": [2042.62, 32563.88, 62314.11, 8144.17, 29971.64, 25210.31],
    "Gross Profit": [3473.05, 167931.47, 210435.89, 139305.83, 233580.68, 247389.69]
}

df_financial = pd.DataFrame(financial_data)
st.dataframe(df_financial)

# Approve Payments Section
st.subheader("Approve Payments")
payments_data = {
    "Vendor ID": [""],
    "Vendor name": [""],
    "Payment amount": [""],
    "Payment status": [""],
    "Payment method": [""]
}
df_payments = pd.DataFrame(payments_data)
st.dataframe(df_payments)

# Resource Assignments Section
st.subheader("Resource Assignments")
assignments_data = {
    "Project ID": ["10000", "10001", "10002", "10003"],
    "Project Name": ["JENTETCH Implementation", "StaffTru Implementation", "Been Verified Implementation", "Grand Financial Implementation"],
    "Resource": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Brown"],
    "Start Date": ["2023-05-01", "2023-05-15", "2023-06-01", "2023-06-15"],
    "End Date": ["2023-07-31", "2023-08-15", "2023-09-30", "2023-10-15"]
}
df_assignments = pd.DataFrame(assignments_data)
st.dataframe(df_assignments)

# Budget vs Actual Chart
st.subheader("Budget vs Actual")
budget_data = {
    "Category": ["Labor", "Materials", "Equipment", "Other"],
    "Budget": [100000, 50000, 30000, 20000],
    "Actual": [95000, 48000, 32000, 18000]
}
df_budget = pd.DataFrame(budget_data)

fig = go.Figure()
fig.add_trace(go.Bar(x=df_budget['Category'], y=df_budget['Budget'], name='Budget'))
fig.add_trace(go.Bar(x=df_budget['Category'], y=df_budget['Actual'], name='Actual'))
fig.update_layout(barmode='group', title='Budget vs Actual Expenses')
st.plotly_chart(fig)

# Footer (placeholder for video controls)
st.write("1:50 / 2:01")
