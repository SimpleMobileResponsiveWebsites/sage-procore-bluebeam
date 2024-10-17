import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide", page_title="ERP Integrations - Job Costs")

    # Header
    st.title("ERP Integrations")
    st.subheader("Job Cost Codes & Cost Types")

    # Main content
    st.header("ACMATACX ERP INTEGRATION JOB COSTS")
    st.write("12345678 - Italian Restaurant Project")

    # Create DataFrame for job costs
    data = {
        "Cost": ["01 - GENERAL REQUIREMENTS", "Division 01 - General R", "01.000 - General Conditions", "01.015 - Project Manager", "01.017 - Project Engineer, Civil Leader", "01.040 - Project Controls", "01.700 - Clean Up", "Division 01 - General R", "02 - EXISTING CONDITIONS", "Division 02 - Existing C", "03 - CONCRETE", "Division 03 - Concrete", "03.100 - Concrete Forming", "03.200 - Concrete Reinforcing", "03.300 - Cast-in-Place Concrete", "03.400 - Precast Concrete", "03.500 - Cementitious Decks", "03.600 - Grouts", "03.700 - Concrete Curing", "03.900 - Concrete Restoration", "Division 03 - Concrete"],
        "Phase ID Subcode": ["", "", "01.000.001", "01.015.001", "01.017.001", "01.040.001", "01.700.001", "", "", "", "", "", "03.100.001", "03.200.001", "03.300.001", "03.400.001", "03.500.001", "03.600.001", "03.700.001", "03.900.001", ""],
        "Original Budget": ["$748,472", "n/a", "$300,000", "$200,000", "$100,000", "$100,000", "$48,472", "n/a", "$0", "n/a", "$1,314,456", "n/a", "$131,446", "$200,000", "$375,000", "$375,000", "$131,446", "$40,000", "$40,000", "$21,564", "n/a"],
        "Current Budget": ["$748,472", "n/a", "$300,000", "$200,000", "$100,000", "$100,000", "$48,472", "n/a", "$350,000", "n/a", "$1,314,456", "n/a", "$131,446", "$200,000", "$375,000", "$375,000", "$131,446", "$40,000", "$40,000", "$21,564", "n/a"],
        "Pending CO": ["$0", "n/a", "$0", "$0", "$0", "$0", "$0", "n/a", "$0", "n/a", "$0", "n/a", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "n/a"],
        "Revised Budget": ["$748,472", "n/a", "$300,000", "$200,000", "$100,000", "$100,000", "$48,472", "n/a", "$350,000", "n/a", "$1,314,456", "n/a", "$131,446", "$200,000", "$375,000", "$375,000", "$131,446", "$40,000", "$40,000", "$21,564", "n/a"],
        "Actual Cost": ["$0", "n/a", "$0", "$0", "$0", "$0", "$0", "n/a", "$0", "n/a", "$0", "n/a", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "n/a"],
        "Committed Cost": ["$0", "n/a", "$0", "$0", "$0", "$0", "$0", "n/a", "$0", "n/a", "$0", "n/a", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "n/a"],
        "Total Cost": ["$0", "n/a", "$0", "$0", "$0", "$0", "$0", "n/a", "$0", "n/a", "$0", "n/a", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "n/a"],
    }
    df = pd.DataFrame(data)

    # Display the DataFrame
    st.dataframe(df, hide_index=True)

    # Sidebar
    with st.sidebar:
        st.subheader("FILTER BY JOB")
        st.text_input("Project")
        st.checkbox("Show Jobs Cost Code greater than $1,000")
        st.button("Search")

if __name__ == "__main__":
    main()
