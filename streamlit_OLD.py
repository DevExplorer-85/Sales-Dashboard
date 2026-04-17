# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Performance Dashboard 2023")

df = pd.read_csv(r'C:\Users\DHRUV\Downloads\amazon.csv\amazon.csv')
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')
df['revenue'] = df['units'] * df['unit_price']

# KPI Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"₹{df['revenue'].sum():,.0f}")
col2.metric("Units Sold", f"{df['units'].sum():,}")
col3.metric("Avg Order Value", f"₹{(df['revenue']/df['units']).mean():,.0f}")
col4.metric("Top Region", df.groupby('region')['revenue'].sum().idxmax())

# Charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Monthly Revenue Trend")
    monthly = df.groupby('month')['revenue'].sum()
    st.line_chart(monthly)

with col_right:
    st.subheader("Revenue by Region")
    region_rev = df.groupby('region')['revenue'].sum()
    st.bar_chart(region_rev)