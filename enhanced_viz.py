import pandas as pd
import plotly.express as px
import os

df = pd.read_csv('data/processed/sales_clean.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# 修正：使用 strftime 聚合，再转回 datetime 确保 Plotly 识别为时间轴
monthly = df.groupby(df['Order_Date'].dt.strftime('%Y-%m'))['Sales'].sum().reset_index()
monthly['Order_Date'] = pd.to_datetime(monthly['Order_Date'])

fig1 = px.line(monthly, x='Order_Date', y='Sales', 
               title='月度销售趋势（交互式）',
               labels={'Sales': '总销售额', 'Order_Date': '月份'})
fig1.update_traces(mode='lines+markers')

top10 = df.groupby('Product')['Sales'].sum().nlargest(10).reset_index()
fig2 = px.bar(top10, x='Sales', y='Product', orientation='h',
              title='销售额 TOP10 产品',
              labels={'Sales': '总销售额', 'Product': '产品名称'})

os.makedirs('outputs', exist_ok=True)
with open('outputs/interactive_report.html', 'w', encoding='utf-8') as f:
    f.write('<h1 style="text-align:center;">零售销售分析看板</h1>')
    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write('<hr style="margin:40px 0;">')
    f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))

print("交互式看板已生成: outputs/interactive_report.html")