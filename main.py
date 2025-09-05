import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Number of menu items
num_items = 10
# Generate synthetic data
data = {
    'MenuItem': [f'Item {i+1}' for i in range(num_items) for _ in range(100)],
    'Date': pd.to_datetime(['2024-01-01'] * 1000),
    'Sales': np.random.randint(10, 100, size=1000),
    'SentimentScore': np.random.uniform(-1, 1, size=1000) # -1: very negative, 1: very positive
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
# --- 2. Data Cleaning and Preparation (Minimal in this synthetic example) ---
# In a real-world scenario, this section would include handling missing values, outliers, etc.
# --- 3. Analysis ---
# Group data by menu item and calculate average sentiment and sales
item_summary = df.groupby('MenuItem').agg({'Sales': 'mean', 'SentimentScore': 'mean'})
# Calculate correlation between sentiment and sales
correlation = item_summary['Sales'].corr(item_summary['SentimentScore'])
print(f"Correlation between average sentiment and average sales: {correlation:.2f}")
# --- 4. Visualization ---
plt.figure(figsize=(10, 6))
sns.regplot(x='SentimentScore', y='Sales', data=item_summary)
plt.title('Correlation between Average Sentiment and Average Sales')
plt.xlabel('Average Sentiment Score')
plt.ylabel('Average Sales')
plt.grid(True)
plt.tight_layout()
# Save the plot to a file
output_filename = 'sentiment_sales_correlation.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Further analysis (example):  Monthly sales trend for the top 3 selling items.
top_3_items = item_summary.sort_values(by='Sales', ascending=False).head(3).index
top_3_sales = df[df['MenuItem'].isin(top_3_items)].groupby(['MenuItem', 'Month'])['Sales'].sum().unstack()
plt.figure(figsize=(12,6))
top_3_sales.plot(kind='bar', figsize=(10,6))
plt.title('Monthly Sales for Top 3 Items')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.legend(title='Menu Item')
plt.xticks(rotation=0)
plt.tight_layout()
output_filename2 = 'top3_monthly_sales.png'
plt.savefig(output_filename2)
print(f"Plot saved to {output_filename2}")