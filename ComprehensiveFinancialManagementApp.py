import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Helper function to create a Gantt chart
def create_gantt_chart():
    df = pd.DataFrame([
        dict(Task="Task 1", Start='2023-01-01', Finish='2023-02-28', Resource="Team A"),
        dict(Task="Task 2", Start='2023-02-15', Finish='2023-04-30', Resource="Team B"),
        dict(Task="Task 3", Start='2023-03-01', Finish='2023-05-31', Resource="Team C"),
    ])
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
    return fig

# Main app
def main():
    st.set_page_config(layout="wide", page_title="Financial Management System")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Projects", "Tasks", "Accounts Payable", "Sales Invoice"])

    if page == "Dashboard":
        show_dashboard()
    elif page == "Projects":
        show_projects()
    elif page == "Tasks":
        show_tasks()
    elif page == "Accounts Payable":
        show_accounts_payable()
    elif page == "Sales Invoice":
        show_sales_invoice()

def show_dashboard():
    st.title("Project Manager Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Projects", "15", "2")
    with col2:
        st.metric("On-time Projects", "12", "-1")
    with col3:
        st.metric("Total Revenue", "$1.2M", "15%")

    st.subheader("Project Status Overview")
    project_status = pd.DataFrame({
        "Project": ["Project A", "Project B", "Project C", "Project D"],
        "Progress": [75, 30, 90, 50],
        "Status": ["On Track", "Delayed", "Ahead", "On Track"]
    })
    st.dataframe(project_status)

    st.subheader("Resource Allocation")
    fig = px.bar(
        x=["Team A", "Team B", "Team C", "Team D"],
        y=[40, 25, 35, 20],
        labels={'x': 'Team', 'y': 'Utilization (%)'}
    )
    st.plotly_chart(fig)

def show_projects():
    st.title("Project Management")
    
    st.subheader("Project Financial Summary")
    financial_summary = pd.DataFrame({
        "Project": ["Project A", "Project B", "Project C"],
        "Budget": ["$100,000", "$150,000", "$200,000"],
        "Actual Cost": ["$90,000", "$160,000", "$180,000"],
        "Variance": ["$10,000", "-$10,000", "$20,000"]
    })
    st.dataframe(financial_summary)

    st.subheader("Project Gantt Chart")
    gantt_chart = create_gantt_chart()
    st.plotly_chart(gantt_chart)

def show_tasks():
    st.title("Task Information")
    
    with st.form("task_form"):
        col1, col2 = st.columns(2)
        with col1:
            project = st.selectbox("Project", ["BigBoxCampaign", "Project B", "Project C"])
            task_id = st.text_input("Task ID")
            task_name = st.text_input("Task Name")
            start_date = st.date_input("Start Date")
        with col2:
            end_date = st.date_input("End Date")
            assignee = st.selectbox("Assignee", ["John Doe", "Jane Smith", "Bob Johnson"])
            status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        
        description = st.text_area("Description")
        submit_button = st.form_submit_button("Save Task")

    if submit_button:
        st.success("Task saved successfully!")

def show_accounts_payable():
    st.title("Accounts Payable")
    
    st.subheader("Bills List")
    bills = pd.DataFrame({
        "Bill ID": ["B001", "B002", "B003"],
        "Vendor": ["Vendor A", "Vendor B", "Vendor C"],
        "Amount": ["$5,000", "$3,500", "$7,200"],
        "Due Date": ["2023-06-15", "2023-06-20", "2023-06-25"],
        "Status": ["Unpaid", "Paid", "Unpaid"]
    })
    st.dataframe(bills)

    st.subheader("Add New Bill")
    with st.form("new_bill_form"):
        vendor = st.selectbox("Vendor", ["Vendor A", "Vendor B", "Vendor C", "Vendor D"])
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        due_date = st.date_input("Due Date")
        submit_button = st.form_submit_button("Add Bill")

    if submit_button:
        st.success("Bill added successfully!")

def show_sales_invoice():
    st.title("Sales Invoice")
    
    with st.form("invoice_form"):
        col1, col2 = st.columns(2)
        with col1:
            customer = st.selectbox("Customer", ["Customer A", "Customer B", "Customer C"])
            invoice_date = st.date_input("Invoice Date")
            due_date = st.date_input("Due Date")
        with col2:
            invoice_number = st.text_input("Invoice Number")
            project = st.selectbox("Project", ["Project A", "Project B", "Project C"])
        
        st.subheader("Invoice Items")
        items = st.data_editor(
            pd.DataFrame({"Item": [""], "Quantity": [0], "Unit Price": [0.0], "Total": [0.0]}),
            num_rows="dynamic"
        )
        
        total_amount = items["Total"].sum()
        st.write(f"Total Amount: ${total_amount:.2f}")
        
        submit_button = st.form_submit_button("Create Invoice")

    if submit_button:
        st.success("Invoice created successfully!")

if __name__ == "__main__":
    main()
