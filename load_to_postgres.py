import urllib.parse
import pandas as pd
from sqlalchemy import create_engine, text

# 1. Load the data
print("📂 Loading data for database insertion...")
df = pd.read_csv("raw_sales_data.csv")
df['unit_price'] = df['unit_price'].fillna(df.groupby('category')['unit_price'].transform('median'))
df['total_sales'] = df['quantity'] * df['unit_price']

# 2. Connect to PostgreSQL
DB_USER = "postgres"
DB_PASSWORD = "venu@123"  # Your actual password with the @ symbol
DB_HOST = "localhost"
DB_PORT = "5432"

# Safely encode password in case it contains special characters like '@'
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)

print("🔌 Connecting to PostgreSQL...")
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/postgres')

# Ensure database 'ecommerce_db' exists
with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
    result = conn.execute(text("SELECT 1 FROM pg_database WHERE datname='ecommerce_db'"))
    if not result.scalar():
        conn.execute(text("CREATE DATABASE ecommerce_db"))
        print("📦 Created database 'ecommerce_db'!")

# Re-connect specifically to 'ecommerce_db'
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/ecommerce_db')

# 3. Load DataFrame into PostgreSQL table
print("🚀 Writing data to PostgreSQL table 'sales_transactions'...")
df.to_sql('sales_transactions', engine, if_exists='replace', index=False)

print("✅ Successfully loaded 1,000 rows into PostgreSQL database 'ecommerce_db'!")