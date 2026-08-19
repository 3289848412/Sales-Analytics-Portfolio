import subprocess
import sys
import os

print("=" * 50)
print("零售销售分析全自动管道")
print("=" * 50)

scripts = [
    ("生成模拟数据", "generate_data.py"),
    ("原始项目：建SQLite库", "src/original_build_db.py"),
    ("原始项目：生成静态Matplotlib图", "src/original_viz.py"),
    ("高阶改造：数据清洗(制造脏数据→清洗)", "src/data_cleaning.py"),
    ("高阶改造：基于清洗数据重建库", "src/build_db_clean.py"),
    ("高阶改造：生成动态Plotly报告", "src/enhanced_viz.py"),
]

for name, script in scripts:
    print(f"\n[{name}] 执行中...")
    try:
        subprocess.run([sys.executable, script], check=True)
    except subprocess.CalledProcessError as e:
        print(f" 脚本 {script} 执行失败，错误码: {e.returncode}")
        sys.exit(1)

print("\n" + "=" * 50)
print("全部完成！请查看以下产出：")
print("   静态图: outputs/basic_report.png")
print("   动态看板: outputs/interactive_report.html")
print("   原始库: data/sales.db  |  清洗库: data/sales_clean.db")
print("   脏数据: data/raw/sales_raw.csv  |  清洗后: data/processed/")
print("=" * 50)