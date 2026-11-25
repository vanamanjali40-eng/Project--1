# Tableau Dashboard Build Guide

## Connect
1. Open Tableau Desktop/Public and connect to `retail_cleaned_data.csv`.
2. Set `Order_Date` to Date and numeric fields to appropriate measures.
3. Create calculated field `Profit Margin`: `SUM([Profit]) / SUM([Revenue])` (format percentage).

## Suggested dashboard layout
- KPI cards: Total Revenue, Total Profit, Profit Margin, Units Sold, Average Inventory Days.
- Bar chart: Profit by Category and Sub-Category.
- Line chart: Monthly Revenue and Profit (Order_Date).
- Scatter plot: Inventory Days vs Profit (Product_ID detail; add trend line).
- Heatmap: Category by Season using Profit or Revenue.
- Table: Product_ID, Category, Units_Sold, Inventory_Days, Revenue, Profit, Margin.

## Filters (apply to all worksheets)
Region, Category, Sub_Category, Season, Order_Date.

## Suggested interactions
Use category/region selections as dashboard filter actions; highlight high inventory days (>90) with a calculated flag.

## Calculated fields
- Profit Margin: `SUM([Profit]) / SUM([Revenue])`
- Inventory Risk: `IF AVG([Inventory_Days]) > 90 THEN 'Slow / Overstock Risk' ELSE 'Normal' END`
- Month: `DATETRUNC('month',[Order_Date])`

Dataset is synthetic. Dashboard findings will be illustrative, not actual retail decisions.
