import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)
random.seed(42)

# Generate 1,000 synthetic e-commerce transactions
data = []
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty']

for i in range(1, 1001):
    order_id = 1000 + i
    customer_id = random.randint(101, 250)  # Generates repeat customers
    order_date = fake.date_between(start_date='-1y', end_date='today')
    category = random.choice(categories)
    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(10.0, 300.0), 2)
    
    # Introduce intentional nulls for data cleaning practice
    if random.random() < 0.05:
        unit_price = None

    data.append({
        "order_id": order_id,
        "customer_id": customer_id,
        "order_date": order_date,
        "category": category,
        "quantity": quantity,
        "unit_price": unit_price
    })

df = pd.DataFrame(data)
df.to_csv("raw_sales_data.csv", index=False)
print("✅ Created 'raw_sales_data.csv' with 1,000 transaction records!")