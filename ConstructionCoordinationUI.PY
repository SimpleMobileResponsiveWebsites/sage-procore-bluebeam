import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def main():
    st.set_page_config(layout="wide", page_title="Coordination Issues")

    # Header
    col1, col2, col3, col4 = st.columns([3,1,1,1])
    with col1:
        st.title("Coordination Issues")
    with col2:
        st.button("Export")
    with col3:
        st.button("Download Plugin")
    with col4:
        st.button("Create Issue", type="primary")

    # Main content
    col1, col2 = st.columns([3,1])

    with col1:
        # Dashboard
        st.subheader("Dashboard")
        
        # Overview and Progress
        col1_1, col1_2, col1_3 = st.columns(3)
        
        with col1_1:
            st.subheader("Overview")
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 38,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Issues"},
                gauge = {'axis': {'range': [None, 50]}}
            ))
            st.plotly_chart(fig, use_container_width=True)

        with col1_2:
            st.subheader("Progress")
            progress_data = pd.DataFrame({
                'Level': ['Level 4', 'Level 3', 'Level 2', 'Level 1'],
                'Complete': [8, 5, 3, 2],
                'In Progress': [2, 3, 4, 5],
                'Not Started': [1, 2, 3, 1]
            })
            fig = px.bar(progress_data, x='Level', y=['Complete', 'In Progress', 'Not Started'], 
                         barmode='stack', orientation='h')
            st.plotly_chart(fig, use_container_width=True)

        with col1_3:
            st.subheader("Ball in Court")
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 18,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Issues"},
                gauge = {'axis': {'range': [None, 50]}}
            ))
            st.plotly_chart(fig, use_container_width=True)

        # Issues Table
        st.subheader("Issues")
        issues_data = {
            "Title": ["Field Issue", "Field Issue", "Drop Duct", "Sprinkler Conflict"],
            "Status": ["Open", "Open", "Open", "Ready for Review"],
            "Priority": ["", "", "", "High"],
            "Assigned Company": ["MECCON, Inc.", "MECCON, Inc.", "Comfortable...", "All Involved Co..."],
            "Assignee": ["Tyler F.", "Tyler F.", "Paul R.", "Stanley F."],
            "Trade": ["", "", "", "Fire Sprinklers"]
        }
        df = pd.DataFrame(issues_data)
        st.dataframe(df, use_container_width=True, hide_index=True)

    with col2:
        # Issue Details
        st.subheader("CI #18")
        st.write("Sprinkler Conflict")
        st.image("https://via.placeholder.com/300x200.png?text=3D+Model+View", use_column_width=True)
        
        st.write("Location: Level 1")
        st.write("Due Date: 5 / 13 / 2021")
        st.write("Priority: High")
        st.write("Assignee: Stanley Ferguson (All-Involved Contracting)")
        st.write("Trade: Fire Sprinklers")

if __name__ == "__main__":
    main()
