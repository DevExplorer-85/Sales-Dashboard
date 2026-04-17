# 📊 Sales Dashboard

> An end-to-end data analytics project exploring discount strategies, customer ratings,
> and pricing patterns across 1,464 Amazon India product listings.

[View Live Dashboard]((https://sales-dashboard2026.streamlit.app/))

# Problem Statement

Amazon India lists thousands of products with varying discount levels — but do higher
discounts actually correlate with better customer ratings? Which categories are being
discounted the most, and which products offer the highest absolute savings?

This dashboard answers these questions through interactive visualizations and data-driven insights


# Key Business Insights

| 1 | Average discount across all products is **47.7%** | Nearly half the catalog is on sale — heavy discount culture |
| 2 | Home Improvement has the highest avg discount (58%) | Possibly clearing slow-moving inventory |
| 3 | Office Products has the lowest discount yet the highest rating | Premium pricing does not hurt perception |
| 4 | "Sony Bravia 65" leads with ₹61,910 off the original price | High-ticket electronics dominate savings charts |
| 5 | Discount distribution is right-skewed (peak at 50–65%) | Most products are discounted above 50% |



# Tech Stack

| Python 3 | Core programming language |
| pandas | Data cleaning and aggregation |
| matplotlib / seaborn | Static chart generation |
| Streamlit | Interactive dashboard framework |
| GitHub | Version control and project hosting |



# Project Structure

```
amazon-sales-dashboard/
│
├── dashboard.py          # Main Streamlit app
├── amazon.csv            # Raw dataset
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

# Dashboard Features

- KPI Tiles— Total products, average discount, highest rated category, max savings
- Avg Discount % by Category — Horizontal bar chart comparing discount intensity
- Avg Rating by Category — Customer satisfaction across product categories  
- Top 10 Products by Savings — Products with the highest absolute price drop in ₹
- Discount Distribution— Histogram with KDE curve showing spread of discounts



# Dataset

- Source: Amazon India product listings (public dataset via Kaggle)
- Size: 1,464 products across 8 categories
- Fields: Product name, category, actual price, discounted price, rating, number of reviews
- Derived columns: Savings (₹), Discount %, Short product name



# How to Run Locally

# 1. Clone the repository
https://github.com/DevExplorer-85/Sales-Dashboard/.git

# 2. Navigate into the project folder
cd amazon-sales-dashboard

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the dashboard
streamlit run dashboard.py
```

Open your browser at [`http://localhost:8501`](https://sales-dashboard2026.streamlit.app/)


##  What I Learned

- End-to-end data analytics workflow — from raw CSV to deployed dashboard
- Data cleaning with pandas — handling nulls, fixing types, deriving new columns
- Building interactive dashboards with Streamlit
- Translating raw numbers into business insights
