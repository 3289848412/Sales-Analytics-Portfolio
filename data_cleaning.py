import pandas as pd
import numpy as np
import os

COL_ORDER_ID = 'Order_ID'
COL_SALES = 'Sales'
COL_PRODUCT = 'Product'
COL_DATE = 'Order_Date'

df = pd.read_csv('data/sales.csv')

# 制造脏数据
df_dirty = df.copy()
np.random.seed(42)

dirty_idx = np.random.choice(df_dirty.index, size=int(0.1 * len(df_dirty)), replace=False)
df_dirty.loc[dirty_idx, COL_SALES] = np.random.choice([-999, np.nan], size=len(dirty_idx))

dup_count = int(0.05 * len(df_dirty))
if dup_count > 0:
    df_dirty.iloc[-dup_count:, df_dirty.columns.get_loc(COL_ORDER_ID)] = \
        df_dirty.iloc[:dup_count, df_dirty.columns.get_loc(COL_ORDER_ID)].values

date_idx = np.random.choice(df_dirty.index, size=int(0.03 * len(df_dirty)), replace=False)
df_dirty.loc[date_idx, COL_DATE] = '1900-01-01'

os.makedirs('data/raw', exist_ok=True)
df_dirty.to_csv('data/raw/sales_raw.csv', index=False)
print("脏数据已保存: data/raw/sales_raw.csv")

# 清洗
df_clean = df_dirty.copy()
df_clean = df_clean.drop_duplicates(subset=[COL_ORDER_ID], keep='first')

median_val = df_clean[df_clean[COL_SALES] > 0][COL_SALES].median()
df_clean[COL_SALES] = df_clean[COL_SALES].apply(
    lambda x: median_val if (pd.isna(x) or x < 0) else x
)

try:
    most_common = df_clean[df_clean[COL_DATE] != '1900-01-01'][COL_DATE].mode()[0]
    df_clean[COL_DATE] = df_clean[COL_DATE].replace('1900-01-01', most_common)
except:
    from datetime import datetime
    df_clean[COL_DATE] = df_clean[COL_DATE].replace('1900-01-01', datetime.today().strftime('%Y-%m-%d'))

df_clean[COL_DATE] = pd.to_datetime(df_clean[COL_DATE], errors='coerce').dt.strftime('%Y-%m-%d')

os.makedirs('data/processed', exist_ok=True)
df_clean.to_csv('data/processed/sales_clean.csv', index=False)
print(f"清洗后数据已保存: data/processed/sales_clean.csv")
print(f"   - 行数变化: {len(df_dirty)} → {len(df_clean)} (删除重复)")
print(f"   - 销售额中位数填充值: {median_val:.2f}")