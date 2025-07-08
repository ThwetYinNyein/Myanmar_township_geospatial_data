from multiprocessing import connection
import psycopg2
import csv
import os
from dotenv import load_dotenv

# PostgreSQL connection setup
#pg_user = os.getenv('Pg_User')
#pg_password = os.getenv('Pg_Password')
#pg_host = os.getenv('Pg_HOST')
#dbt = 'product_bi'

config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}
CSV_FILE = "township_summary_updated.csv"

# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(**config)
    cursor = conn.cursor()
    print("Connected to PostgreSQL database.")
except psycopg2.Error as err:
    print(f"PostgreSQL connection error: {err}")
    exit(1)

create_table_query = """
CREATE TABLE IF NOT EXISTS tsp_geo_area (
    id SERIAL PRIMARY KEY,
    township_name TEXT,
    township_code TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    area_km2 DOUBLE PRECISION
);
"""
cursor.execute(create_table_query)
conn.commit()

# === READ AND INSERT CSV DATA ===
with open(CSV_FILE, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            cursor.execute("""
                INSERT INTO tsp_geo_area (township_name, township_code, latitude, longitude, area_km2)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                row['Township_Name'],
                row['Township_Code'],
                float(row['Latitude']),
                float(row['Longitude']),
                float(row['Area_km2'])
            ))
        except Exception as e:
            print(f"Failed to insert row {row}: {e}")
conn.commit()
# Close PostgreSQL connection
if cursor:
    cursor.close()
if conn:
    conn.close()
    print("PostgreSQL connection closed.")

print("CSV data imported successfully into PostgreSQL.")
