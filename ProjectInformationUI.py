import streamlit as st
from datetime import date

def main():
    st.set_page_config(layout="wide")
    st.title("Project Information")

    # Tabs
    tabs = st.tabs(["Project", "Additional info", "Resources & pricing", "Project summary", "Invoice options", "Assessment"])

    with tabs[0]:  # Project tab
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Project ID", key="project_id")
            st.text_input("Project name", key="project_name")
            st.selectbox("Product category", [""], key="product_category")
            st.selectbox("Contract", [""], key="contract")
            st.selectbox("Project type", [""], key="project_type")
            st.text_area("Description", key="description")
        
        with col2:
            st.selectbox("Customer", [""], key="customer")
            st.date_input("Begin date", key="begin_date")
            st.date_input("End date", key="end_date")
            st.selectbox("Parent project", [""], key="parent_project")
            st.checkbox("Invoice with parent", key="invoice_with_parent")

        # Project Status
        st.subheader("Project Status")
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Project status", [""], key="project_status")
        with col2:
            st.selectbox("Status", ["Active"], key="status")

        # People
        st.subheader("People")
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Project manager", [""], key="project_manager")
            st.selectbox("External user (customer)", [""], key="external_user")
        with col2:
            st.selectbox("Sales contact", [""], key="sales_contact")

        # Business Rules
        st.subheader("Business Rules")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Timesheet and expense user restrictions")
            option = st.radio(
                "",
                ["Use system configuration option",
                 "Time can be entered by any user",
                 "Only users assigned to the project can enter time",
                 "Only users assigned to the project and task can enter time"],
                key="timesheet_restrictions"
            )
        
        with col2:
            st.write("Transaction rules")
            st.text_input("Transaction rule name", key="transaction_rule_name")
            st.button("Add rule")

    # Placeholder for other tabs
    for tab in tabs[1:]:
        with tab:
            st.write("Content for this tab is not implemented in this example.")

    # Save and Cancel buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Save"):
            st.success("Project information saved successfully!")
    with col2:
        if st.button("Cancel"):
            st.warning("Changes discarded.")

if __name__ == "__main__":
    main()
