from sqlalchemy import create_engine, text

# Connect directly to your 'ecommerce_db' database
DB_USER = "postgres"
DB_PASSWORD = "postgres123"  # Your new password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce_db"

print("🔌 Connecting to PostgreSQL to run SQL queries...")
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

with engine.connect() as conn:
    print("\n==============================")
    print("📊 SQL BUSINESS INSIGHTS")
    print("==============================\n")

    # 1. Overall Summary Query
    summary_query = text("""
        SELECT COUNT(*) AS total_orders, 
               SUM(total_sales) AS overall_revenue,
               AVG(total_sales) AS avg_order_value
        FROM sales_transactions;
    """)
    summary = conn.execute(summary_query).fetchone()
    print(f"📦 Total Orders in DB: {summary[0]:,}")
    print(f"💰 Overall Revenue:    ${summary[1]:,.2f}")
    print(f"📈 Average Order Value: ${summary[2]:,.2f}")

    # 2. Top Categories Query
    print("\n🏆 Top Product Categories by Revenue (via SQL):")
    category_query = text("""
        SELECT category, 
               COUNT(*) AS order_count, 
               SUM(total_sales) AS category_revenue
        FROM sales_transactions
        GROUP BY category
        ORDER BY category_revenue DESC;
    """)
    results = conn.execute(category_query)
    for row in results:
        print(f"   - {row[0]}: ${row[2]:,.2f} ({row[1]} orders)")

print("\n🚀 SQL querying complete successfully!")