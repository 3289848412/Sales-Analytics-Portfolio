import sqlite3
import pandas as pd
import os

df = pd.read_csv('data/processed/sales_clean.csv')
conn = sqlite3.connect('data/sales_clean.db')
df.to_sql('sales', conn, if_exists='replace', index=False)
conn.close()
print("清洗后数据库已创建: data/sales_clean.db")