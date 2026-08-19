import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(2026)

dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')

products = ['iPhone 15', 'Samsung S24', 'Sony WH-1000', 'Dell XPS 13', 'MacBook Pro',
            'iPad Air', 'Galaxy Tab', 'Nikon Z6', 'Canon R5', 'DJI Mini 4']
categories = ['Electronics', 'Accessories', 'Camera']

data = {
    'Order_ID': [],
    'Order_Date': [],
    'Product': [],
    'Category': [],
    'Sales': [],
    'Quantity': []
}

for i in range(5000):
    if np.random.rand() > 0.6:
        date_idx = np.random.randint(365, len(dates))
    else:
        date_idx = np.random.randint(0, 365)
    
    order_date = dates[date_idx]
    product = np.random.choice(products)
    category = np.random.choice(categories)
    quantity = np.random.randint(1, 6)
    unit_price = np.random.uniform(100, 2000)
    sales = round(unit_price * quantity, 2)
    
    data['Order_ID'].append(f'ORD-{i+1:05d}')
    data['Order_Date'].append(order_date.strftime('%Y-%m-%d'))
    data['Product'].append(product)
    data['Category'].append(category)
    data['Sales'].append(sales)
    data['Quantity'].append(quantity)

df = pd.DataFrame(data)
os.makedirs('data', exist_ok=True)
df.to_csv('data/sales.csv', index=False)
print("模拟数据已生成: data/sales.csv (共 5000 条订单)")