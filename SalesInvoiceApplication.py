import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Sales Invoice", layout="wide")

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
        height: 2em;
        padding: 0rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("Sales Invoice")

# Buttons
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.button("Print/Email")
with col2:
    st.button("Done")
with col3:
    st.button("More actions")

# Tabs
tab1, tab2, tab3 = st.tabs(["Transaction", "History", "Payment details"])

with tab1:
    # Invoice details
    st.subheader("Intelligent Audit (10000)")
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.metric("Transaction date", "07/07/2019")
    col2.metric("Date due", "08/06/2019")
    col3.metric("Item totals", "26,120.00")
    col4.metric("Subtotals", "0.90")
    col5.metric("Transaction total", "26,120.00")
    col6.metric("Transaction status", "Pending")
    col7.metric("Payment status", "Open")

    # Other details
    col1, col2 = st.columns(2)
    with col1:
        st.write("Date: 07/07/2019")
        st.write("Customer: 10000 - Intelligent Audit")
        st.write("Project:")
        st.write("Document number: IN00127")
        st.write("Payment terms: Net 30")
        st.write("Date due: 08/06/2019")
        st.write("Reference:")
        st.write("Message:")
        st.write("Ship via:")

    with col2:
        st.write("GL posting date: 07/07/2019")
        st.write("Bill to:")
        st.write("Intelligent Audit#C10000")
        st.write("336 West Passaic Street")
        st.write("Rochelle Park, NJ 07662 United States")
        st.write("Ship to:")
        st.write("Intelligent Audit#C10000")
        st.write("336 West Passaic Street")
        st.write("Rochelle Park, NJ 07662 United States")
        st.write("Attachments:")
        st.write("Base currency: USD")
        st.write("Tax currency: USD")
        st.write("Exchange rate date: 07/07/2019")
        st.write("Exchange rate type:")
        st.write("Exchange rate:")
        st.write("State: Pending")
        st.write("Customer PO number: -")

    # Entries
    st.subheader("Entries")
    entries_data = {
        "Item #": [""],
        "Description": [""],
        "Quantity": [""],
        "Unit": [""],
        "Price": [""],
        "Discount %": [""],
        "Account": [""],
        "Tax": [""],
        "Amount": [""],
        "": [""]
    }
    df = pd.DataFrame(entries_data)
    st.dataframe(df, height=100)

    # Total
    st.write("Total: $ 26,120.00")

# Placeholder for other tabs
with tab2:
    st.write("History tab content")

with tab3:
    st.write("Payment details tab content")

# Footer (placeholder)
st.write("1:47 / 3:01")
