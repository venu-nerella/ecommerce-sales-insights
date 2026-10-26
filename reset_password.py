from sqlalchemy import create_engine, text

# Connect without a password using the temporary 'trust' setting
engine = create_engine('postgresql+psycopg2://postgres:@localhost:5432/postgres')

with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
    conn.execute(text("ALTER USER postgres WITH PASSWORD 'postgres123';"))
    print("✅ Successfully reset PostgreSQL password to 'postgres123'!")