import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(page_title="Cubit Services Financials - Task Information", layout="wide")

# Custom CSS for layout
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .stTextInput > div > div > input {
        background-color: #f0f0f0;
    }
    .stSelectbox > div > div > select {
        background-color: #f0f0f0;
    }
    .stDateInput > div > div > input {
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.image("https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png", width=100)
with col2:
    st.title("Cubit Services Financials")
with col3:
    st.write("CLIENT USA")

# Navigation
st.sidebar.title("Navigation")
st.sidebar.button("Projects")

# Main content
st.header("Task Information")

# Tabs
tab1, tab2, tab3 = st.tabs(["Task", "Additional info", "Resource scheduling"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Project")
        st.selectbox("", ["BigAirCampaign"])
        
        st.subheader("Standard task")
        st.selectbox("Standard task", [""])
        
        st.subheader("Task ID *")
        st.text_input("Task ID", "")
        
        st.subheader("Name *")
        st.text_input("Name", "")
        
        st.subheader("Project begin date")
        st.date_input("Project begin date", datetime(2020, 2, 26))
        
        st.subheader("Project end date")
        st.date_input("Project end date", datetime(2020, 5, 27))
        
        st.subheader("Planned begin date")
        st.date_input("Planned begin date", datetime(2020, 2, 26))
    
    with col2:
        st.subheader("Planned end date")
        st.date_input("Planned end date", datetime(2020, 5, 27))
        
        st.subheader("Dependent on task")
        st.selectbox("Dependent on task", [""])
        
        st.subheader("Task Alias")
        st.text_input("Task Alias", "")
        
        st.subheader("Item")
        st.selectbox("Item", [""])
        
        st.subheader("Billable")
        st.checkbox("Billable")
        
        st.subheader("Description")
        st.text_area("Description", "")

# Footer (placeholder for video controls)
st.write("1:21 / 3:01")
