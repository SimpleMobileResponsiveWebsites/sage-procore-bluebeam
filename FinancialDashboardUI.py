import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def main():
    st.set_page_config(layout="wide", page_title="Cubit Services Financials")

    # Header
    col1, col2, col3, col4 = st.columns([3,1,1,1])
    with col1:
        st.title("Cubit Services Financials")
    with col2:
        st.button("CUBIT USA")
    with col3:
        st.write("Zoey G")
    with col4:
        st.write("Help & Support")

    # Navigation
    st.sidebar.button("⭐")
    st.sidebar.button("🏠")
    st.sidebar.button("Dashboards")

    # Main content
    tab1, tab2 = st.tabs(["Dashboards", "Reports"])

    with tab1:
        col1, col2, col3 = st.columns([2,2,3])
        
        with col1:
            st.subheader("Dashboards")
            options = ["All", "Projects", "Tasks", "Timesheets", "Expenses", "Invoicing", "Accounts Payable", "Accounts Receivable", "Resource Management"]
            for option in options:
                st.checkbox(option, value=True if option == "All" else False)

        with col2:
            st.subheader("Setup")
            setup_options = ["Customers", "Employees", "Items", "Project & resource mgmt", "My favorites", "Staff resources"]
            for option in setup_options:
                st.checkbox(option)

        with col3:
            st.subheader("Overview")
            fig = go.Figure(go.Indicator(
                mode = "number+delta",
                value = 18742,
                delta = {"reference": 16582, "valueformat": ".0f"},
                title = {"text": "All Hours"},
                domain = {'y': [0, 1], 'x': [0.25, 0.75]}))
            st.plotly_chart(fig, use_container_width=True)

    # Sample data for tables
    vendor_data = {
        "Vendor ID": [1, 2, 3],
        "Vendor name": ["Vendor A", "Vendor B", "Vendor C"],
        "Payment amount": ["$1000", "$2000", "$1500"],
        "Payment status": ["Paid", "Pending", "Paid"],
        "Payment method": ["Bank Transfer", "Check", "Bank Transfer"]
    }
    vendor_df = pd.DataFrame(vendor_data)

    budget_data = {
        "Customer": ["Customer A", "Customer B", "Customer C"],
        "Project ID": ["P001", "P002", "P003"],
        "Project Name": ["Project X", "Project Y", "Project Z"],
        "Budgeted Amount": ["$10,000", "$15,000", "$12,000"],
        "Actual Amount": ["$9,500", "$14,800", "$12,200"]
    }
    budget_df = pd.DataFrame(budget_data)

    timesheet_data = {
        "Project ID": ["P001", "P002", "P003"],
        "Project Name": ["Project X", "Project Y", "Project Z"],
        "Task Name": ["Task 1", "Task 2", "Task 3"],
        "Employee Name": ["John Doe", "Jane Smith", "Bob Johnson"],
        "Start Date": ["2023-05-01", "2023-05-02", "2023-05-03"],
        "End Date": ["2023-05-05", "2023-05-06", "2023-05-07"],
        "Hours": [40, 35, 38]
    }
    timesheet_df = pd.DataFrame(timesheet_data)

    st.subheader("Vendor Information")
    st.dataframe(vendor_df)

    st.subheader("Budget vs Actual")
    st.dataframe(budget_df)

    st.subheader("Timesheet")
    st.dataframe(timesheet_df)

if __name__ == "__main__":
    main()
