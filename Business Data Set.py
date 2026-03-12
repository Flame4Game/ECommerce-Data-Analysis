import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"ecommerce_sales_data.csv")
df = df.dropna()
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Subsection"] = (((df["Order Date"].dt.year) - 2022) * 2) + (df["Order Date"].dt.month.apply(lambda x: 0 if x <= 6 else 1)) + 1
df["Profit per Sale"] = (df["Profit"]/df["Sales"])
df.to_csv(r"ecommerce_added_columns.csv", index=False)
df.dropna()
pivot = df.pivot_table(
    values='Profit per Sale',
    index='Product Name',
    columns='Region',
    aggfunc='mean'
)
pivot["Overall"] = pivot.mean(axis=1)
pivot.loc["Overall"] = pivot.mean()
sns.heatmap(pivot, annot=True, fmt='.4f', cmap='RdYlGn')
plt.title('Profit per Sale by Region and Product Name')
plt.show()