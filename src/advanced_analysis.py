import sqlite3
import os
import csv

DB_PATH = "data/sales_clean.db"
SQL_PATH = "src/advanced_queries.sql"

# 与 advanced_queries.sql 中语句顺序一一对应
OUTPUTS = [
    ("月度产品排名 TOP3", "outputs/monthly_product_rank.csv"),
    ("月度销售额环比增长", "outputs/monthly_growth.csv"),
]


def main():
    with open(SQL_PATH, encoding="utf-8") as f:
        sql_text = f.read()

    # 去掉注释后按分号切分为多条独立语句
    statements = [s.strip() for s in sql_text.split(";") if s.strip()]

    conn = sqlite3.connect(DB_PATH)
    os.makedirs("outputs", exist_ok=True)

    for i, stmt in enumerate(statements):
        cur = conn.execute(stmt)
        cols = [d[0] for d in cur.description]
        rows = cur.fetchall()

        if i < len(OUTPUTS):
            label, filename = OUTPUTS[i]
        else:
            label, filename = f"查询 {i + 1}", f"outputs/query_{i + 1}.csv"

        print(f"\n[{label}] 执行结果（共 {len(rows)} 行）")
        print(" | ".join(cols))
        for row in rows:
            print(" | ".join(str(v) for v in row))

        with open(filename, "w", newline="", encoding="utf-8-sig") as fh:
            writer = csv.writer(fh)
            writer.writerow(cols)
            writer.writerows(rows)
        print(f"结果已保存: {filename}")

    conn.close()
    print("\nSQL 窗口函数分析完成。")


if __name__ == "__main__":
    main()
