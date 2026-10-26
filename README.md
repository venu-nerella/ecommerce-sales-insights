# 🚀 E-Commerce Sales Insights: Cloud Data Product

An end-to-end cloud-deployed data engineering and analytics pipeline built with **Python, Pandas, SQLAlchemy, Neon PostgreSQL, and Streamlit**. This application transforms raw e-commerce transaction data into a production-ready, interactive intelligence dashboard hosted in the cloud.

---

## 🏗️ Architecture & Tech Stack

* **Data Processing & ETL**: Python, Pandas (data cleansing, imputation, transformation)
* **Database**: Neon (Serverless PostgreSQL) with connection pooling and secure SSL
* **ORM & Database Connection**: SQLAlchemy, `psycopg2-binary`
* **Web Application & UI**: Streamlit Community Cloud
* **Version Control**: Git & GitHub

---

## 📊 Key Features

* **Cloud-Native Database Storage**: Migrated from local SQLite/Postgres to a robust, serverless cloud PostgreSQL instance hosted on Neon.
* **Automated Data Hygiene**: Handles missing values (e.g., median imputation by category) and computes dynamic metrics like total sales.
* **Interactive Analytics Dashboard**: Real-time visualization of sales trends, top-performing categories, and regional performance.
* **Secure Production Configuration**: Utilizes Streamlit Cloud Secrets and environment variable management for credential security.

---

## 🛠️ Local Development & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/venu-nerella/ecommerce-sales-insights.git](https://github.com/venu-nerella/ecommerce-sales-insights.git)
   cd ecommerce-sales-insights
   ```
2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: .\venv\Scripts\Activate.ps1
      ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
      ```   

4. **Configure your database connection**:
   ```bash
   $env:DATABASE_URL="your_neon_connection_string"   
```
5. **Seed the database & run the app**:
   ```bash
   python load_to_postgres.py
   streamlit run app.py
```

---

## 🌐 Live Demo
Check out the live production application deployed on Streamlit Cloud: [E-Commerce Sales Insights Hub](https://venu-nerella-ecommerce-sales-insights.streamlit.app)
