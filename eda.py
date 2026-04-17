import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

# --- Data Load & Clean (datacleaning.py wali steps repeat karni padti hain) ---
df = pd.read_csv(r'C:\Users\DHRUV\Downloads\amazon.csv\amazon.csv')

# Price columns clean karo
df['discounted_price']    = df['discounted_price'].str.replace('[₹,]', '', regex=True).astype(float)
df['actual_price']        = df['actual_price'].str.replace('[₹,]', '', regex=True).astype(float)
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=True).astype(float)
df['rating']              = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count']        = df['rating_count'].str.replace(',', '', regex=True)
df['rating_count']        = pd.to_numeric(df['rating_count'], errors='coerce')
df['savings']             = df['actual_price'] - df['discounted_price']

df = df.drop_duplicates()
df = df.dropna(subset=['actual_price', 'discounted_price', 'rating'])

# --- EDA ---

# 1. Average discounted price
print("Avg Discounted Price: ₹", round(df['discounted_price'].mean(), 2))

# 2. Average rating
print("Avg Rating:", round(df['rating'].mean(), 2))

# 3. Revenue (savings) by category
print("\n--- Top Categories by Avg Discount % ---")
cat_discount = df.groupby('category')['discount_percentage'].mean().sort_values(ascending=False)
print(cat_discount.head(10))

# 4. Top 5 highest rated products
print("\n--- Top 5 Highest Rated Products ---")
top_rated = df[['product_name', 'rating', 'rating_count']].sort_values('rating', ascending=False).head(5)
print(top_rated.to_string(index=False))

# 5. Top 5 biggest savings products
print("\n--- Top 5 Biggest Savings Products ---")
top_savings = df[['product_name', 'actual_price', 'discounted_price', 'savings']].sort_values('savings', ascending=False).head(5)
print(top_savings.to_string(index=False))

# 6. Discount distribution
print("\n--- Discount % Distribution ---")
print(df['discount_percentage'].describe())