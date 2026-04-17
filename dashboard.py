import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Amazon Sales Dashboard", layout="wide")
st.title("🛒 Amazon India - Sales Dashboard")

# --- Load & Clean Data ---
@st.cache_data
def load_data():
    df = pd.read_csv(r'C:\Users\DHRUV\Downloads\amazon.csv\amazon.csv')
    df['discounted_price']    = df['discounted_price'].str.replace('[₹,]', '', regex=True).astype(float)
    df['actual_price']        = df['actual_price'].str.replace('[₹,]', '', regex=True).astype(float)
    df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=True).astype(float)
    df['discount_pct']        = df['discount_percentage']  # alias
    df['rating']              = pd.to_numeric(df['rating'], errors='coerce')
    df['rating_count']        = df['rating_count'].str.replace(',', '', regex=True)
    df['rating_count']        = pd.to_numeric(df['rating_count'], errors='coerce')
    df['savings']             = df['actual_price'] - df['discounted_price']
    df['short_name']          = df['product_name'].str[:35] + '...'
    df['main_category']       = df['category'].str.split('|').str[0]
    df = df.drop_duplicates().dropna(subset=['actual_price', 'discounted_price', 'rating'])
    return df


df = load_data()

# --- KPI Row ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Products",         f"{len(df):,}")
col2.metric("Avg Discount",           f"{df['discount_pct'].mean():.1f}%")
col3.metric("Highest Rated Category", df.groupby('category')['rating'].mean().idxmax())
col4.metric("Max Saving",             f"₹{df['savings'].max():,.0f}")

st.divider()

# --- Charts Row 1 ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Avg Discount % by Category")
    cat_discount = df.groupby('main_category')['discount_percentage'].mean().sort_values(ascending=False).head(8)
    st.bar_chart(cat_discount)

with col_right:
    st.subheader("⭐ Avg Rating by Category")
    cat_rating = df.groupby('main_category')['rating'].mean().sort_values(ascending=False).head(8)
    st.bar_chart(cat_rating)

st.divider()

# --- Charts Row 2 ---
col_left2, col_right2 = st.columns(2)

with col_left2:
    st.subheader("💰 Top 10 Products by Savings (₹)")
    top_savings = df.nlargest(10, 'savings')[['short_name', 'actual_price', 'discounted_price', 'savings']]
    st.dataframe(top_savings, use_container_width=True)

with col_right2:
    st.subheader("📈 Discount % Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['discount_percentage'], bins=20, kde=True, color='steelblue', ax=ax)
    ax.set_xlabel("Discount %")
    st.pyplot(fig)

st.divider()

# --- Raw Data ---
with st.expander("🔍 View Raw Data"):
    st.dataframe(df, use_container_width=True)
