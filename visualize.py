import sys
sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Data Load & Clean ---
df = pd.read_csv(r'C:\Users\DHRUV\Downloads\amazon.csv\amazon.csv')
df['discounted_price']    = df['discounted_price'].str.replace('[₹,]', '', regex=True).astype(float)
df['actual_price']        = df['actual_price'].str.replace('[₹,]', '', regex=True).astype(float)
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=True).astype(float)
df['rating']              = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count']        = df['rating_count'].str.replace(',', '', regex=True)
df['rating_count']        = pd.to_numeric(df['rating_count'], errors='coerce')
df['savings']             = df['actual_price'] - df['discounted_price']
df['main_category']       = df['category'].str.split('|').str[0]  # top-level category
df = df.drop_duplicates().dropna(subset=['actual_price', 'discounted_price', 'rating'])

# --- Data for charts ---
cat_discount  = df.groupby('main_category')['discount_percentage'].mean().sort_values(ascending=False).head(8)
cat_rating    = df.groupby('main_category')['rating'].mean().sort_values(ascending=False).head(8)
top_savings   = df.nlargest(8, 'savings')[['product_name', 'savings']]
top_savings['product_name'] = top_savings['product_name'].str[:40] + '...'

# --- Plot ---
sns.set_style("darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle('Amazon India - Sales Dashboard', fontsize=18, fontweight='bold', y=1.01)

# Chart 1: Avg Discount % by Category (bar)
sns.barplot(x=cat_discount.values, y=cat_discount.index, ax=axes[0,0], palette='Blues_r')
axes[0,0].set_title('Avg Discount % by Category')
axes[0,0].set_xlabel('Discount %')
axes[0,0].set_ylabel('')

# Chart 2: Avg Rating by Category (bar)
sns.barplot(x=cat_rating.values, y=cat_rating.index, ax=axes[0,1], palette='Greens_r')
axes[0,1].set_title('Avg Rating by Category')
axes[0,1].set_xlabel('Rating')
axes[0,1].set_xlim(3.5, 5)
axes[0,1].set_ylabel('')

# Chart 3: Top 8 Products by Savings (horizontal bar)
sns.barplot(x=top_savings['savings'], y=top_savings['product_name'], ax=axes[1,0], palette='Oranges_r')
axes[1,0].set_title('Top 8 Products - Biggest Savings (₹)')
axes[1,0].set_xlabel('Savings (₹)')
axes[1,0].set_ylabel('')

# Chart 4: Discount % Distribution (histogram)
sns.histplot(df['discount_percentage'], bins=20, ax=axes[1,1], color='steelblue', kde=True)
axes[1,1].set_title('Discount % Distribution')
axes[1,1].set_xlabel('Discount %')
axes[1,1].set_ylabel('Count')

plt.tight_layout()
plt.savefig('sales_dashboard.png', dpi=150, bbox_inches='tight')
print("Chart saved as sales_dashboard.png")
plt.show()