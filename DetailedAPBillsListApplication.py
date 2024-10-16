import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Cubit Services Financials", layout="wide")

# Custom CSS for layout
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .stSelectbox>div>div>select {
        padding: 0rem 1rem;
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
    st.write("Karla Grace")
    st.write("Help & Support")

# Sidebar
with st.sidebar:
    st.header("Reporting as")
    
    # Folder structure
    st.subheader("AP Bills")
    st.checkbox("All Bill Ledger", value=True)
    st.checkbox("Attributes")
    
    folders = [
        "1099 [AP bill spec]",
        "AP Account title [A]",
        "AP account [AP bi]",
        "Account [AP bill s]",
        "Account label [AP",
        "Allocation [AP bil",
        "Base currency [AP"
    ]
    for folder in folders:
        st.checkbox(folder, key=folder)
    
    st.subheader("Shared")
    st.selectbox("Show:", ["All"])
    st.checkbox("Shared Folders")
    
    st.subheader("Views")
    st.button("Title")
    st.button("Date")

# Main content
st.header("AP Bills List")

# Toolbar
col1, col2, col3, col4 = st.columns(4)
with col1:
    date_type = st.selectbox("Date type selected:", ["Bill date"])
with col2:
    date_selected = st.date_input("Date Selected:", datetime(2019, 12, 31))
with col3:
    max_rows = st.selectbox("Max rows selected:", ["30"])
with col4:
    st.button("🔍")
    st.button("📊")

# Create sample data
data = {
    "Vendor name": ["Archer Technologies"] + ["Boston Properties"] * 10,
    "Bill number": ["075601"] + [f"V0000{i}" for i in range(1, 11)],
    "Bill amount": [1000.00] + [6850.62] * 10,
    "Status": ["Paid"] * 11,
    "Total paid": [1000.00] + [6851.00] * 10,
    "Bill date": ["12/31/2019"] + ["3/1/2018"] * 10,
    "Due date": ["12/31/2019"] + ["3/31/2018"] * 10,
    "Date fully paid": ["12/31/2019"] + ["3/31/2018"] * 10,
    "Days to pay": [1.00] + [30.00] * 10,
    "Memo": [""] * 11,
    "Days overdue": [-1134] + list(range(1740, 1750))
}

df = pd.DataFrame(data)

# Display dataframe
st.dataframe(df, height=400)

# Footer
st.write("2:32 / 3:01")

# Additional controls (placeholder)
col1, col2, col3 = st.columns(3)
with col1:
    st.button("⏪")
with col2:
    st.button("▶")
with col3:
    st.button("⏩")
