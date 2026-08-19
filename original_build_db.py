import sqlite3
import pandas as pd
import os

df = pd.read_csv('data/sales.csv')
conn = sqlite3.connect('data/sales.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS sales')
cursor.execute('''
CREATE TABLE sales (
    Order_ID TEXT PRIMARY KEY,
    Order_Date TEXT,
    Product TEXT,
    Category TEXT,
    Sales REAL,
    Quantity INTEGER
)
''')

df.to_sql('sales', conn, if_exists='append', index=False)
conn.commit()
conn.close()
print("原始数据库已创建: data/sales.db")