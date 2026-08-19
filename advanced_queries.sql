-- 月度产品排名（ROW_NUMBER）
WITH monthly_rank AS (
    SELECT 
        Product,
        strftime('%Y-%m', Order_Date) AS month,
        SUM(Sales) AS total_sales,
        ROW_NUMBER() OVER (PARTITION BY strftime('%Y-%m', Order_Date) ORDER BY SUM(Sales) DESC) AS rn
    FROM sales
    GROUP BY Product, month
)
SELECT month, Product, total_sales
FROM monthly_rank
WHERE rn <= 3
ORDER BY month ASC, total_sales DESC;

-- 月度环比增长率（LAG）
WITH monthly_total AS (
    SELECT 
        strftime('%Y-%m', Order_Date) AS month,
        SUM(Sales) AS current_month_sales
    FROM sales
    GROUP BY month
)
SELECT 
    month,
    current_month_sales,
    LAG(current_month_sales, 1) OVER (ORDER BY month) AS prev_month_sales,
    ROUND((current_month_sales - LAG(current_month_sales, 1) OVER (ORDER BY month)) 
          / LAG(current_month_sales, 1) OVER (ORDER BY month) * 100, 2) || '%' AS growth_rate
FROM monthly_total
ORDER BY month ASC;