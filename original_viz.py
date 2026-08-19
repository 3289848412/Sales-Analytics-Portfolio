import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect('data/sales.db')

monthly = pd.read_sql_query('''
    SELECT strftime('%Y-%m', Order_Date) AS month, SUM(Sales) AS sales
    FROM sales
    GROUP BY month
    ORDER BY month
''', conn)

top_products = pd.read_sql_query('''
    SELECT Product, SUM(Sales) AS sales
    FROM sales
    GROUP BY Product
    ORDER BY sales DESC
    LIMIT 10
''', conn)

conn.close()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.plot(monthly['month'], monthly['sales'], marker='o', color='royalblue')
ax1.set_title('Monthly Sales Trend (Static)', fontsize=14)
ax1.set_xlabel('Month')
ax1.set_ylabel('Total Sales')
ax1.tick_params(axis='x', rotation=45)

ax2.barh(top_products['Product'], top_products['sales'], color='tomato')
ax2.set_title('Top 10 Products by Sales', fontsize=14)
ax2.set_xlabel('Total Sales')
ax2.invert_yaxis()

plt.tight_layout()
os.makedirs('outputs', exist_ok=True)
plt.savefig('outputs/basic_report.png', dpi=150)
print("静态报告已生成: outputs/basic_report.png")