# Sales-Analytics-Portfolio
# 零售销售数据自动化分析管道

## 项目简介
本项目独立构建了一套完整的零售销售分析 Pipeline，覆盖数据生成、质量治理（制造脏数据并清洗）、数据库建模（SQLite）、进阶指标计算（SQL窗口函数）及交互式报告产出全流程。

## 主要
- **数据治理**：主动构造缺失值、负值、重复ID三类脏数据，采用中位数填充和去重策略完成清洗。
- **进阶分析**：运用 ROW_NUMBER 和 LAG 窗口函数实现月度产品排名及销售环比增长计算。
- **工程化**：编写一键运行脚本（run.py），实现数据到报告的全链路自动化闭环。

## 在线看板
[点击查看交互式销售看板](https://3289848412.github.io/Sales-Analytics-Portfolio/)

## 技术栈
`Python` `Pandas` `SQLite` `Matplotlib` `Plotly` `SQL窗口函数`

## 本地运行
```bash
pip install -r requirements.txt
python run.py
