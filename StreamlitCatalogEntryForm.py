import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Catalog Item Entry Form", layout="wide")
    
    # Title
    st.title("Add Catalog Item")
    
    # Create two columns for the form layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Essential Details")
        
        # Dropdown for type selection
        item_type = st.selectbox("Type", ["Part", "Assembly", "System", "Equipment", "Subcontractor", "Fixed", "Labor"])
        
        # Text inputs for catalog details
        catalog_number = st.text_input("Catalog Number")
        description = st.text_area("Description")
        
        # Toggle buttons for status
        st.write("Status")
        status_col1, status_col2 = st.columns(2)
        with status_col1:
            active_status = st.toggle("Active", value=True)
        with status_col2:
            inactive_status = st.toggle("Inactive")
    
    with col2:
        st.subheader("Catalog Details")
        
        # Additional catalog information
        manufacturer = st.text_input("Manufacturer")
        supplier = st.text_input("Supplier")
        catalog_notes = st.text_area("Catalog Notes")
        unit_price = st.number_input("Unit Price", min_value=0.0, step=0.01)
        
        # File uploader for attachment
        st.subheader("Attachment")
        st.file_uploader("Upload PDF specification (optional)", type=['pdf'])
    
    # Bottom action buttons
    col1, col2, col3 = st.columns([6, 1, 1])
    with col2:
        st.button("Cancel")
    with col3:
        st.button("Save", type="primary")

if __name__ == "__main__":
    main()
