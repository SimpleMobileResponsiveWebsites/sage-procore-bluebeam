import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide", page_title="Task Information")

    # Header
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.button("⭐")  # Star button
        st.button("🏠")  # Home button
    with col2:
        st.selectbox("Projects", [""])
    with col3:
        st.button("Search")

    # Task Information header
    st.header("Task Information")

    # Tabs
    tabs = st.tabs(["Task", "Additional info", "Resource scheduling"])

    with tabs[0]:  # Task tab
        st.subheader("Task Info")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text_input("Task ID")
        with col2:
            st.text_input("Name")
        with col3:
            st.text_input("Parent task ID")

        # Resource Search and Schedule buttons
        col1, col2 = st.columns(2)
        with col1:
            st.button("Resource Search")
        with col2:
            st.button("Resource Schedule")

        # Project resources table
        st.subheader("Project resources")
        
        # Create a sample dataframe for the project resources
        df = pd.DataFrame({
            "": [1, 2],
            "Task resources": ["", ""],
            "Description": ["", ""],
            "Start date": ["", ""],
            "End date": ["", ""],
            "Estimated hours": ["", ""],
            "Planned hours": ["", ""],
            "Staff book": ["", ""],
            "Full time": ["", ""],
            "Actual hours": ["", ""],
            "Appv hours": ["", ""],
            "Actual start": ["", ""],
            "Est % compl": ["", ""]
        })

        # Display the dataframe as an editable table
        edited_df = st.data_editor(df, num_rows="dynamic", hide_index=True)

    with tabs[1]:  # Additional info tab
        st.write("Additional info content goes here")

    with tabs[2]:  # Resource scheduling tab
        st.write("Resource scheduling content goes here")

if __name__ == "__main__":
    main()
