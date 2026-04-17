import pandas as pd

df = pd.read_csv(r'C:\Users\DHRUV\Downloads\amazon.csv\amazon.csv')

# Step 1: Understand the data
print(df.shape)        # how many rows/cols
print(df.dtypes)       # what type is each column
print(df.isnull().sum()) # find missing values
print(df.head())

# Step 2: Fix data types (price columns clean karenge)
# '₹' aur ',' remove karke numeric banao
df['discounted_price'] = df['discounted_price'].str.replace('[₹,]', '', regex=True).astype(float)
df['actual_price']     = df['actual_price'].str.replace('[₹,]', '', regex=True).astype(float)
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=True).astype(float)
df['rating']           = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count']     = df['rating_count'].str.replace(',', '', regex=True)
df['rating_count']     = pd.to_numeric(df['rating_count'], errors='coerce')

# Step 3: Remove duplicates
df = df.drop_duplicates()

# Step 4: Handle nulls (drop or fill)
df = df.dropna()  # or df.fillna(0) for numeric cols

# Step 5: Add useful columns
df['savings']           = df['actual_price'] - df['discounted_price']
df['discount_category'] = pd.cut(df['discount_percentage'], bins=[0,25,50,75,100], labels=['Low','Medium','High','Very High'])

print('\n--- Cleaned Data ---')
print(df[['product_name','actual_price','discounted_price','discount_percentage','rating']].head())
print('\nData types after cleaning:')
print(df.dtypes)