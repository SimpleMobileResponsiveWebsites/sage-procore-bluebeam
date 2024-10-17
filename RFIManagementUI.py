import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide", page_title="RFIs by status")

    # Header
    col1, col2, col3 = st.columns([3,1,1])
    with col1:
        st.title("RFIs by status")
    with col3:
        st.button("Export")

    # Main content
    col1, col2 = st.columns([3,1])

    with col1:
        # Chart options
        st.write("Description Title: RFIs by status")
        chart_types = ["Bar", "Pie", "Line", "Column", "Area"]
        selected_chart = st.selectbox("Type of chart", chart_types, index=0)

        # Filter options
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            st.selectbox("From", ["All"] + [f"Option {i}" for i in range(1, 6)])
        with filter_col2:
            st.selectbox("To", ["All"] + [f"Option {i}" for i in range(1, 6)])
        
        st.button("Reset")
        st.button("Apply")

        # RFI Table
        st.subheader("RFI List")
        rfi_data = {
            "RFI #": ["1"],
            "Subject": ["Plans Electrical Sub RFI"],
            "Assignee": ["Hal Project Manager"],
            "Question": ["In Drawing S1.01, there is a discrepancy with the framing in Lighting Section A. Can you please clarify the correct framing detail for this area?"],
            "Response": ["Please see attached and revised drawing showing where beam supporting the floor above is located. Let me know if you have any additional questions."],
            "Status": ["Closed"],
        }
        df = pd.DataFrame(rfi_data)
        st.dataframe(df, use_container_width=True)

    with col2:
        # Action buttons
        action_buttons = [
            "Edit", "PDF", "Distribution Matrix", 
            "Sync Report", "Close", "Delete"
        ]
        for button in action_buttons:
            st.button(button, key=button, use_container_width=True)
        
        # General report links
        st.subheader("GENERAL REPORT LINKS")
        report_links = ["Reports", "Distribution History"]
        for link in report_links:
            st.markdown(f"* {link}")

if __name__ == "__main__":
    main()
