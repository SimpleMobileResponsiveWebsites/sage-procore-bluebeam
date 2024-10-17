import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide", page_title="ERP Integrations")

    # Header
    st.title("ERP Integrations")

    # Subheader navigation
    st.markdown("""
    <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
        <span>ERP Cost Codes & Cost Types</span>
        <span>Vendors</span>
        <span>Sub Jobs</span>
        <span>Budgets</span>
        <span>Commitments</span>
        <span>Committed Change Orders</span>
        <span>Job Costs</span>
        <span>Equipment/Labor Imports</span>
    </div>
    """, unsafe_allow_html=True)

    # Info box
    st.info("ProCore ERP Integration appears to be fully synced. Latest Sage 300 CRE project cost data has been retrieved as displayed in the items below.")

    # Main content title
    st.subheader("ACMATACX ERP INTEGRATION COSTS READY TO BE IMPORTED")

    # Create DataFrame for project costs
    data = {
        "Account/WBS/Job Cost": ["PB000010", "DPP978-003", "JCX001", "20000080-1001", "750101", "HB0001-01", "JP0001"],
        "Project Name": ["D23 Nature", "Three Rivers Development", "DT01 Nightlife", "NOMA Water Management", "Project Sample01", "Heart Care Renovation", "Downtown Project"],
        "Total Estimate": ["$0.00", "$784,978.00", "$0.00", "$30,000.00", "$50,000.00", "$0.00", "$2,000.00"],
    }
    df = pd.DataFrame(data)

    # Display the DataFrame
    st.dataframe(df, hide_index=True)

    # Add action buttons to each row
    for i in range(len(df)):
        cols = st.columns([4, 1, 1])
        with cols[1]:
            st.button("Import", key=f"import_{i}")
        with cols[2]:
            st.button("Ignore", key=f"ignore_{i}")

    # Sidebar
    with st.sidebar:
        st.subheader("FILTER BY PROJECT KEY")
        st.text_input("Project To Import ID")
        st.text_input("Period To Import ID")
        st.text_input("Amount")
        st.button("Search")
        st.button("Clear", type="secondary")

if __name__ == "__main__":
    main()
