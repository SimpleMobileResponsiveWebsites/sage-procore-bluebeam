import streamlit as st

def main():
    st.title("Project Management UI")

    # Contract and Project Type
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Contract", [""])
        st.selectbox("Project type", [""])
        st.text_area("Description", height=100)
    
    with col2:
        st.selectbox("Parent project", [""])
        st.checkbox("Invoice with parent")

    # Project Status
    st.subheader("Project Status")
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Project status", [""])
    with col2:
        st.selectbox("Status", ["Active"])

    # People
    st.subheader("People")
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Project manager", [""])
        st.selectbox("External user (customer)", [""])
    with col2:
        st.selectbox("Sales contact", [""])

    # Business Rules
    st.subheader("Business Rules")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Timesheet and expense user restrictions")
        option = st.radio(
            "",
            ["Use system configuration option",
             "Time can be entered by any user",
             "Only users assigned to the project can enter time",
             "Only users assigned to the project and task can enter time"]
        )
    
    with col2:
        st.write("Transaction rules")
        st.text_input("Transaction rule name")
        st.button("Add rule")

if __name__ == "__main__":
    main()
