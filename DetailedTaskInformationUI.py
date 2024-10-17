import streamlit as st
from datetime import date

def main():
    st.set_page_config(layout="wide", page_title="Cubit Services Financials")

    # Header
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.image("https://via.placeholder.com/50x50.png?text=Logo", width=50)
    with col2:
        st.title("Cubit Services Financials")
    with col3:
        st.button("CUBIT USA")

    # Navigation
    col1, col2, col3 = st.columns([1,1,4])
    with col1:
        st.button("⭐")
    with col2:
        st.button("🏠")
    with col3:
        st.selectbox("Projects", [""])

    # Task Information header
    st.header("Task Information")

    # Tabs
    tabs = st.tabs(["Task", "Additional info", "Resource scheduling"])

    with tabs[0]:  # Task tab
        col1, col2 = st.columns(2)
        
        with col1:
            st.text("Project")
            st.text("BigBoxCampaign")
            
            st.selectbox("Standard task", [""])
            
            st.text_input("Task ID *")
            
            st.text_input("Name *")
            
            st.text("Project begin date")
            st.text("02/26/2020")
            
            st.text("Project end date")
            st.text("05/27/2020")
            
            st.date_input("Planned begin date", value=date(2020, 2, 26))

        with col2:
            st.date_input("Planned end date", value=date(2020, 5, 27))
            
            st.selectbox("Dependent on task", [""])
            
            st.text_input("Task Alias")
            
            st.selectbox("Item", [""])
            
            st.checkbox("Billable")
            
            st.text_area("Description")

    with tabs[1]:  # Additional info tab
        st.write("Additional info content goes here")

    with tabs[2]:  # Resource scheduling tab
        st.write("Resource scheduling content goes here")

if __name__ == "__main__":
    main()
