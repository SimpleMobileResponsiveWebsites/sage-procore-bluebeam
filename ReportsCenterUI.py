import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide", page_title="Qubi Services Financials")

    # Header
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.image("https://via.placeholder.com/50x50.png?text=Logo", width=50)
    with col2:
        st.title("Qubi Services Financials")
    with col3:
        st.write("Zoey G")
        st.write("Help & Support")

    # Navigation
    st.sidebar.button("Home")
    st.sidebar.button("Reports")

    # Main content
    st.header("Reports Center")
    
    # New Report button
    st.button("New Report")

    # Search bar
    st.text_input("Search")

    # Reports table
    reports = [
        "Project Financial Analysis",
        "Project Financials Summary by PM_RS",
        "Project Financial Summary All PM",
        "Project Financial Summary by PM",
        "Project Financial Summary Canada",
        "Project Financial Summary PM & Group",
        "Project Financial Summary US",
        "Project Profitability",
        "Project target",
        "Realization by Total Hours",
        "Realization by Utilized Hours",
        "Realization by Utilized Hours Canada",
        "Revenue by Customer",
        "Revenue by Item and Customer",
        "Revenue Top 5 Customers",
        "Services Revenue by Customer Project & Item",
        "Transaction Indirect Costs",
        "Transaction Labor Revenue WIP",
        "Utilization by Office",
        "Utilization by Office with Target",
        "Utilization by Office with Target Canada",
        "Utilization Detail",
        "Billings by Customer - US"
    ]

    df = pd.DataFrame({
        "Report Name": reports,
        "Edit": ["Edit" if i < 3 else "" for i in range(len(reports))],
        "Export as": ["Export as ▼" for _ in reports],
        "More actions": ["More actions ▼" for _ in reports]
    })

    # Custom CSS to style the dataframe
    st.markdown("""
    <style>
    .dataframe {font-size: 12px !important;}
    </style>
    """, unsafe_allow_html=True)

    # Display the dataframe
    st.dataframe(df, hide_index=True)

if __name__ == "__main__":
    main()
