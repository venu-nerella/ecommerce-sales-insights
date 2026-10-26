from sqlalchemy import create_engine, text

# Connect to your existing database
DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce_db"

print("🔌 Connecting to PostgreSQL for Advanced SQL analysis...")
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

with engine.connect() as conn:
    print("\n========================================")
    print("📈 PHASE 1: ADVANCED SQL & WINDOW FUNCTIONS")
    print("========================================\n")

    # 1. CTE & Window Function: Running Total of Revenue over Orders
    running_total_query = text("""
        WITH ordered_sales AS (
            SELECT 
                order_id,
                order_date,
                category,
                total_sales,
                ROW_NUMBER() OVER (ORDER BY order_date, order_id) as transaction_seq
            FROM sales_transactions
        )
        SELECT 
            transaction_seq,
            order_id,
            category,
            total_sales,
            SUM(total_sales) OVER (ORDER BY transaction_seq ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_revenue
        FROM ordered_sales
        LIMIT 5;
    """)
    
    print("1️⃣ Running Total & Cumulative Revenue (First 5 Transactions):")
    results = conn.execute(running_total_query)
    for row in results:
        print(f"   - Order #{row[1]} ({row[2]}): ${row[3]:,.2f} | Cumulative Revenue: ${row[4]:,.2f}")

    # 2. Window Function: Category Ranking by Total Sales
    ranking_query = text("""
        SELECT 
            category,
            COUNT(order_id) as total_orders,
            SUM(total_sales) as category_revenue,
            RANK() OVER (ORDER BY SUM(total_sales) DESC) as revenue_rank
        FROM sales_transactions
        GROUP BY category;
    """)
    
    print("\n2️⃣ Category Performance Ranking (Using RANK() Window Function):")
    rank_results = conn.execute(ranking_query)
    for row in rank_results:
        print(f"   - Rank #{row[3]}: {row[0]} with ${row[2]:,.2f} across {row[1]} orders")

print("\n✨ Advanced SQL queries executed successfully!")