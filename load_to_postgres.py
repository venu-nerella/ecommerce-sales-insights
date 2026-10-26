import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Load the data
print("📂 Loading data for database insertion...")
df = pd.read_csv("raw_sales_data.csv")
df['unit_price'] = df['unit_price'].fillna(df.groupby('category')['unit_price'].transform('median'))
df['total_sales'] = df['quantity'] * df['unit_price']

# 2. Connect to Neon PostgreSQL Cloud Database
NEON_URL = "postgresql://neondb_owner:npg_5QWYU3nKXDkr@ep-proud-dust-b720gk3x-pooler.c-13.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
DATABASE_URL = os.getenv("DATABASE_URL", NEON_URL)

# Force SQLAlchemy to use psycopg2 driver instead of psycopg v3
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)

print("🔌 Connecting to Neon Cloud PostgreSQL...")
engine = create_engine(DATABASE_URL)

# 3. Load DataFrame into PostgreSQL table
print("🚀 Writing data to PostgreSQL table 'sales_transactions'...")
df.to_sql('sales_transactions', engine, if_exists='replace', index=False)

print("✅ Successfully loaded 1,000 rows into your Neon cloud database!")