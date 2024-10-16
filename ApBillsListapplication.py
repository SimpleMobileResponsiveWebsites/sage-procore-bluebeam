import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Cubit Services Financials", layout="wide")

# Header
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.image("https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png", width=100)  # Replace with actual logo
with col2:
    st.title("Cubit Services Financials")
with col3:
    st.write("CLIENT USA")
    st.write("Karla Grace")
    st.write("Help & Support")

# Navigation
st.sidebar.title("Navigation")
st.sidebar.button("Reports")

# Main content
st.header("AP Bills List")

# Date filters
col1, col2 = st.columns(2)
with col1:
    date_type = st.selectbox("Date type selected:", ["Bill date"])
with col2:
    date_selected = st.date_input("Date Selected:", datetime.now())

# Create sample data
data = {
    "Vendor name": ["Archer Technologies"] + ["Boston Properties"] * 10,
    "Bill number": ["075601"] + [f"V0000{i}" for i in range(1, 11)],
    "Bill amount": [1000.00] + [6,850.62] * 10,
    "Status": ["Paid"] * 11,
    "Total paid": [1000.00] + [6,851.00] * 10,
    "Bill date": ["12/31/2019"] + ["3/1/2018"] * 10,
    "Due date": ["12/31/2019"] + ["3/31/2018"] * 10,
    "Date fully paid": ["12/31/2019"] + ["3/31/2018"] * 10,
    "Days to pay": [1.00] + [30.00] * 10,
    "Memo": [""] * 11,
    "Days overdue": [-1134] + list(range(1740, 1750))
}

df = pd.DataFrame(data)

# Display dataframe
st.dataframe(df)

# Footer
st.write("2:32 / 3:01")
