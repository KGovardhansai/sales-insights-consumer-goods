# sales_insights.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")

# Merge datasets
sales_data = sales.merge(customers, on="Customer_ID").merge(products, on="Product_ID")

# Basic exploration
print("Sales Data Overview:")
print(sales_data.head())

# Total revenue by region
region_sales = sales_data.groupby("Region")["Revenue"].sum().reset_index()
print("\nRevenue by Region:\n", region_sales)

# Visualization: Revenue by Region
plt.figure(figsize=(8,5))
sns.barplot(x="Region", y="Revenue", data=region_sales, palette="viridis")
plt.title("Revenue by Region")
plt.show()

# Top 5 products by revenue
top_products = sales_data.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products by Revenue:\n", top_products)

# Visualization: Top Products
plt.figure(figsize=(8,5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top 5 Products by Revenue")
plt.ylabel("Revenue")
plt.show()

# Customer segmentation by income
plt.figure(figsize=(8,5))
sns.histplot(sales_data["Income"], bins=10, kde=True, color="orange")
plt.title("Customer Income Distribution")
plt.show()




