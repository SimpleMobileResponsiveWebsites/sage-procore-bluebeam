import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def main():
    st.set_page_config(layout="wide", page_title="Task Management")

    # Header
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        st.title("Tasks")
    with col2:
        st.button("New Task")
    with col3:
        st.button("Settings")

    # Task Details Section
    st.subheader("Task Details")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Task Title")
        st.text_area("Description")
    with col2:
        st.selectbox("Assignee", ["John Doe", "Jane Smith", "Bob Johnson"])
        st.date_input("Due Date")
    
    # Status and Priority
    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
    with col2:
        st.selectbox("Priority", ["Low", "Medium", "High"])
    with col3:
        st.button("Save")

    # Progress Bar
    st.progress(50)

    # Task List
    st.subheader("Task List")
    task_data = {
        "Task Title": [
            "User Experience Optimization",
            "Backend API Development",
            "Database Schema Design"
        ],
        "Assignee": ["John Doe", "Jane Smith", "Bob Johnson"],
        "Due Date": [
            (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
            (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d"),
            (datetime.now() + timedelta(days=21)).strftime("%Y-%m-%d")
        ],
        "Status": ["In Progress", "Not Started", "Completed"],
        "Priority": ["High", "Medium", "Low"]
    }
    df = pd.DataFrame(task_data)
    st.dataframe(df, use_container_width=True)

    # Pagination
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("Page 1 of 5")

if __name__ == "__main__":
    main()
