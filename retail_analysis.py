# Retail Business Performance & Profitability Analysis
# Run: python retail_analysis.py (requires pandas, seaborn, matplotlib)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('retail_cleaned_data.csv', parse_dates=['Order_Date'])
print('Dataset shape:', df.shape)
print(df.describe(include='all'))

# Profitability metrics
category_metrics = df.groupby('Category', dropna=False).agg(
    Revenue=('Revenue','sum'), Profit=('Profit','sum'),
    Avg_Inventory_Days=('Inventory_Days','mean'), Units=('Units_Sold','sum'))
category_metrics['Margin_pct'] = 100 * category_metrics['Profit'] / category_metrics['Revenue']
print(category_metrics.sort_values('Profit', ascending=False))

# Pearson correlation between inventory days and profit (transaction-level)
correlation = df[['Inventory_Days','Profit']].corr(method='pearson').iloc[0,1]
print('Correlation (Inventory_Days vs Profit):', correlation)

# Visualize relationship
sns.regplot(data=df, x='Inventory_Days', y='Profit', scatter_kws={'alpha':0.4})
plt.title(f'Inventory Days vs Profit (r={correlation:.2f})')
plt.tight_layout(); plt.savefig('inventory_profit_correlation.png', dpi=150); plt.show()

# Charts for Tableau planning / Python EDA
sns.barplot(data=df, x='Category', y='Profit', estimator=sum)
plt.xticks(rotation=30); plt.title('Profit by Category'); plt.tight_layout()
plt.savefig('profit_by_category.png', dpi=150); plt.show()

monthly = df.groupby(df['Order_Date'].dt.to_period('M'))[['Revenue','Profit']].sum().reset_index()
monthly['Order_Date'] = monthly['Order_Date'].astype(str)
sns.lineplot(data=monthly, x='Order_Date', y='Revenue'); plt.xticks(rotation=60)
plt.title('Monthly Revenue Trend'); plt.tight_layout()
plt.savefig('monthly_revenue.png', dpi=150); plt.show()
