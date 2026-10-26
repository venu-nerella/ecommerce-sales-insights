import pandas as pd

# 1. Load the raw sales data CSV we just created
print("📂 Loading raw_sales_data.csv...")
df = pd.read_csv("raw_sales_data.csv")

# 2. Data Cleaning: Inspect missing values
print(f"Total rows before cleaning: {len(df)}")
missing_prices_count = df['unit_price'].isnull().sum()
print(f"⚠️ Found {missing_prices_count} rows with missing unit prices.")

# Fill missing unit prices with the median price of that specific category
df['unit_price'] = df['unit_price'].fillna(df.groupby('category')['unit_price'].transform('median'))
print("✅ Data cleaning complete: Missing prices filled with category medians.")

# 3. Feature Engineering: Calculate Total Sales per transaction
df['total_sales'] = df['quantity'] * df['unit_price']

# 4. Business Insights & Analytics
total_revenue = df['total_sales'].sum()
print("\n====================")
print(f"💰 TOTAL REVENUE: ${total_revenue:,.2f}")
print("====================")

print("\n📊 Top Product Categories by Revenue:")
category_sales = df.groupby('category')['total_sales'].sum().reset_index()
category_sales = category_sales.sort_values(by='total_sales', ascending=False)
for index, row in category_sales.iterrows():
    print(f"   - {row['category']}: ${row['total_sales']:,.2f}")

print("\n🚀 Project 1 analysis complete successfully!")