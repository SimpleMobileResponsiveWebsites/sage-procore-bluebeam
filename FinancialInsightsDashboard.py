import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def main():
    st.set_page_config(layout="wide", page_title="Financial Insights")

    # Header
    st.title("Financial Insights")

    # Top menu
    menu_items = ["All", "R2C", "Approved Cost", "Any Plan", "Owner Invoices", "Payments", "Subcontractor Invoices", "Projects by Stage"]
    st.selectbox("View", menu_items)

    # Main content
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        # New Prime Contracts chart
        st.subheader("New Prime Contracts (last 12 months)")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        values = [0.5, 1.2, 0.8, 1.5, 0.3, 1.8, 0.6, 1.1, 0.9, 1.3, 0.7, 1.6]
        fig = go.Figure(data=[go.Bar(x=months, y=values)])
        fig.add_trace(go.Scatter(x=months, y=[1.0]*12, mode='lines', name='Target'))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Top 5 Clients
        st.subheader("Top 5 Clients")
        clients = ['Client A', 'Client B', 'Client C', 'Client D', 'Client E']
        values = [30, 25, 20, 15, 10]
        fig = px.bar(x=values, y=clients, orientation='h')
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        # Top 5 Contract Holders
        st.subheader("Top 5 Contract Holders")
        holders = ['Holder A', 'Holder B', 'Holder C', 'Holder D', 'Holder E']
        values = [35, 28, 18, 12, 7]
        fig = px.pie(values=values, names=holders)
        st.plotly_chart(fig, use_container_width=True)

    # Lower section
    col1, col2 = st.columns(2)

    with col1:
        # Owner Invoices
        st.subheader("Owner Invoices (last 12 months)")
        fig = go.Figure()
        fig.add_trace(go.Bar(x=months, y=[random.uniform(1, 5) for _ in range(12)], name='Invoiced'))
        fig.add_trace(go.Scatter(x=months, y=[random.uniform(3, 7) for _ in range(12)], mode='lines+markers', name='Cumulative'))
        st.plotly_chart(fig, use_container_width=True)

        # Owner Invoices vs. Payments
        st.subheader("Owner Invoices vs. Payments (last 12 months)")
        fig = go.Figure()
        fig.add_trace(go.Bar(x=months, y=[random.uniform(1, 5) for _ in range(12)], name='Invoiced'))
        fig.add_trace(go.Bar(x=months, y=[random.uniform(1, 5) for _ in range(12)], name='Paid'))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Owner Payments
        st.subheader("Owner Payments")
        payments = ['0-30 Days', '31-60 Days', '61-90 Days', '91+ Days']
        values = [5, 3, 2, 1]
        fig = px.bar(x=payments, y=values)
        st.plotly_chart(fig, use_container_width=True)

        # Subcontractor Invoices
        st.subheader("Subcontractor Invoices (last 12 months)")
        fig = go.Figure()
        fig.add_trace(go.Bar(x=months, y=[random.uniform(1, 5) for _ in range(12)], name='Invoiced'))
        fig.add_trace(go.Scatter(x=months, y=[random.uniform(3, 7) for _ in range(12)], mode='lines+markers', name='Cumulative'))
        st.plotly_chart(fig, use_container_width=True)

    # Sidebar
    st.sidebar.subheader("Filters")
    st.sidebar.multiselect("Company", ["Company A", "Company B", "Company C"])
    st.sidebar.multiselect("Project", ["Project 1", "Project 2", "Project 3"])
    st.sidebar.multiselect("Project Status", ["Active", "Completed", "On Hold"])
    st.sidebar.date_input("Start Date")
    st.sidebar.date_input("End Date")

if __name__ == "__main__":
    main()
