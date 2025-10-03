import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the database (or create it)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the customer table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    join_date TEXT
)
''')

# Create the sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product TEXT,
    amount REAL,
    sale_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
''')

# Insert sample data into the customer table
customers = [
    ('Alice', 'alice@example.com', '2024-01-01'),
    ('Bob', 'bob@example.com', '2024-01-02'),
    ('Charlie', 'charlie@example.com', '2024-01-03'),
    ('Diana', 'diana@example.com', '2024-01-04'),
    ('Eve', 'eve@example.com', '2024-01-05')
]

cursor.executemany('''
INSERT INTO customer (name, email, join_date) VALUES (?, ?, ?)
''', customers)

# Insert sample data into the sales table
start_date = datetime(2024, 1, 1)
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']

sales = []
for i in range(30):
    customer_id = random.randint(1, 5)
    product = random.choice(products)
    amount = round(random.uniform(10.0, 100.0), 2)
    sale_date = start_date + timedelta(days=random.randint(0, 29))
    sales.append((customer_id, product, amount, sale_date.strftime('%Y-%m-%d')))

cursor.executemany('''
INSERT INTO sales (customer_id, product, amount, sale_date) VALUES (?, ?, ?, ?)
''', sales)

# Commit the changes
conn.commit()

# Query the data to verify insertion
cursor.execute('SELECT * FROM customer')
print('Customer Table:')
for row in cursor.fetchall():
    print(row)

cursor.execute('SELECT * FROM sales')
print('\nSales Table:')
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
