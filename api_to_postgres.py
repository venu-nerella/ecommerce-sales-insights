import json
import urllib.request
import pandas as pd
from sqlalchemy import create_engine
import datetime

# 1. Database Connection Configuration
DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce_db"

print("🌍 Fetching live product data from public e-commerce API...")
url = "https://dummyjson.com/products?limit=50"

# Request live data with a User-Agent header to bypass 403 blocks
try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response:
        response_data = json.loads(response.read().decode('utf-8'))
        products = response_data['products']
    print(f"✅ Successfully retrieved {len(products)} live products from API!")
except Exception as e:
    print(f"❌ Error fetching from API: {e}")
    exit()

# 2. Data Wrangling & Transformation
df = pd.DataFrame(products)

# Select and rename columns for our data warehouse schema
df_clean = df[['id', 'title', 'category', 'price', 'rating', 'stock']].copy()
df_clean.rename(columns={'id': 'api_product_id'}, inplace=True)

# Add a timestamp for tracking ingestion time
df_clean['ingested_at'] = datetime.datetime.now()

print("🧹 Data transformation complete: Schema mapped successfully.")

# 3. Load into PostgreSQL
print("🔌 Connecting to PostgreSQL...")
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

print("🚀 Writing live API dataset into PostgreSQL table 'external_products'...")
df_clean.to_sql('external_products', engine, if_exists='replace', index=False)

print("🎉 Pipeline Success: Live API data safely stored in database table 'external_products'!")