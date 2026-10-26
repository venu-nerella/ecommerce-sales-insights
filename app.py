import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Page Configuration
st.set_page_config(page_title="E-Commerce Data Intelligence Hub", page_icon="🛍️", layout="wide")

# Database Connection
DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce_db"

@st.cache_resource
def get_engine():
    return create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

engine = get_engine()

# App Header
st.title("🛍️ E-Commerce & Data Engineering Intelligence Hub")
st.markdown("Production-grade data pipeline dashboard powered by **PostgreSQL**, **Python**, and **Streamlit**.")

# Load Data from PostgreSQL
@st.cache_data
def load_data():
    sales_df = pd.read_sql("SELECT * FROM sales_transactions", engine)
    external_df = pd.read_sql("SELECT * FROM external_products", engine)
    return sales_df, external_df

sales_df, external_df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Analytics")
selected_category = st.sidebar.selectbox("Select Product Category", ["All"] + list(sales_df['category'].unique()))

if selected_category != "All":
    filtered_sales = sales_df[sales_df['category'] == selected_category]
else:
    filtered_sales = sales_df

# Top-level Metrics
total_revenue = filtered_sales['total_sales'].sum()
total_orders = len(filtered_sales)
avg_order_value = filtered_sales['total_sales'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
col2.metric("📦 Total Orders", f"{total_orders:,}")
col3.metric("📈 Avg Order Value", f"${avg_order_value:,.2f}")

st.markdown("---")

# Visualizations / Tables Section
tab1, tab2 = st.tabs(["📊 Sales Performance", "🌍 Live API Products (External Catalog)"])

with tab1:
    st.subheader("Category Revenue Breakdown")
    category_summary = filtered_sales.groupby('category')['total_sales'].sum().reset_index()
    st.bar_chart(category_summary.set_index('category'))
    
    st.subheader("Recent Sales Transactions")
    st.dataframe(filtered_sales[['order_id', 'order_date', 'category', 'quantity', 'unit_price', 'total_sales']].head(10), use_container_width='stretch')

with tab2:
    st.subheader("Live External Products Ingested from API")
    st.markdown("This dataset was pulled dynamically via our automated API-to-Database ingestion pipeline.")
    st.dataframe(external_df, use_container_width='stretch')