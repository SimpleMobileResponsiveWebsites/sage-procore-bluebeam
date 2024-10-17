import streamlit as st
from PIL import Image

def main():
    st.set_page_config(layout="wide", page_title="Future Cares Children's Hospital")

    # Header
    st.title("Future Cares Children's Hospital")

    # Main content
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        # 3D Visualization (placeholder)
        st.image("https://via.placeholder.com/800x600.png?text=3D+Building+Visualization", use_column_width=True)
        
        # Navigation buttons
        col1_1, col1_2 = st.columns(2)
        with col1_1:
            st.button("Walk")
        with col1_2:
            st.button("Up/Down")

        # Floor plan
        st.image("https://via.placeholder.com/400x300.png?text=Floor+Plan", width=200)

    with col2:
        # Navigation Views
        st.subheader("Navigation Views")
        st.checkbox("Concrete Pours", value=True)
        levels = ["Level 01", "Level 02", "Level 03", "Level 04", "Roof"]
        for level in levels:
            st.checkbox(level)

    with col3:
        # Inspections
        st.subheader("Inspections")
        st.write("4/4 Fields Visible")
        for i in range(4):
            st.checkbox("Required", key=f"required_{i}")

        st.button("Add Custom Field")
        st.button("Save", type="primary")

    # Sidebar
    with st.sidebar:
        st.subheader("Tools")
        tools = ["Select", "Pan", "Zoom", "Measure", "Section", "Hide"]
        for tool in tools:
            st.button(tool)

if __name__ == "__main__":
    main()
