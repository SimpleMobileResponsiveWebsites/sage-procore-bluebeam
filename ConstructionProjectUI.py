import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.set_page_config(layout="wide")
    
    # Sidebar
    with st.sidebar:
        st.title("Project Navigator")
        st.button("Home")
        st.button("Reports")
        st.button("Calendar")
        st.button("Files")
        st.button("Photos")
        
        st.subheader("Project Tasks")
        tasks = [
            "Foundation Work",
            "Framing",
            "Electrical",
            "Plumbing",
            "HVAC Installation",
            "Drywall",
            "Painting",
            "Flooring",
            "Finish Carpentry"
        ]
        for task in tasks:
            st.checkbox(task)

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("Floor Plan View")
        # Placeholder for floor plan image
        st.image("https://via.placeholder.com/800x600.png?text=Floor+Plan", use_column_width=True)
        
        # Tools below the floor plan
        tool_cols = st.columns(5)
        tool_cols[0].button("Select")
        tool_cols[1].button("Pan")
        tool_cols[2].button("Zoom")
        tool_cols[3].button("Measure")
        tool_cols[4].button("More")

    with col2:
        st.subheader("Task Details")
        task_df = pd.DataFrame({
            "Task": ["HVAC-1001", "ELEC-2023", "PLUMB-3045"],
            "Status": ["In Progress", "Pending", "Completed"],
            "Due Date": ["2024-10-25", "2024-11-05", "2024-10-15"]
        })
        st.dataframe(task_df, use_container_width=True)
        
        st.subheader("Notes")
        st.text_area("Add a note", height=100)
        st.button("Save Note")

if __name__ == "__main__":
    main()
