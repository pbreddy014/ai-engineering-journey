import pandas as pd

sales = pd.read_csv("business_sales.csv")

print("\nDATASET INFORMATION")
print(sales.info())

print("\nSTATISTICS")
print(sales.describe())

print("\nMISSING VALUES")
print(sales.isnull().sum())

print("\nDUPLICATES")
print(sales.duplicated().sum())

sales = sales.drop_duplicates()

sales = sales.rename(columns={
    "Units": "Units_Sold",
    "Price": "Unit_Price",
    "Cost": "Unit_Cost"
})

sales["Revenue"] = (
    sales["Units_Sold"] * sales["Unit_Price"]
)

sales["Total_Cost"] = (
    sales["Units_Sold"] * sales["Unit_Cost"]
)

sales["Profit"] = (
    sales["Revenue"] - sales["Total_Cost"]
)

sales["Profit_Margin"] = (
    sales["Profit"] / sales["Revenue"] * 100
)

total_revenue = sales["Revenue"].sum()
total_cost = sales["Total_Cost"].sum()
total_profit = sales["Profit"].sum()
average_profit = sales["Profit"].mean()
overall_margin = (
    total_profit / total_revenue * 100
)

print("\n===== BUSINESS SUMMARY =====")

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Cost: ${total_cost:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Profit: ${average_profit:,.2f}")
print(f"Overall Profit Margin: {overall_margin:.2f}%")

best_product = sales.loc[
    sales["Profit"].idxmax()
]

print("\n===== BEST PRODUCT =====")

print("Product:", best_product["Product"])
print(f"Profit: ${best_product['Profit']:,.2f}")
print(f"Margin: {best_product['Profit_Margin']:.2f}%")

product_ranking = sales.sort_values(
    "Profit",
    ascending=False
)

print("\n===== PRODUCT RANKING =====")

print(
    product_ranking[
        ["Product", "Revenue", "Profit", "Profit_Margin"]
    ]
)


region_summary = sales.groupby("Region").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Cost=("Total_Cost", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean"),
    Product_Count=("Product", "count")
)

region_summary = region_summary.sort_values(
    "Total_Profit",
    ascending=False
)

print("\n===== REGIONAL ANALYSIS =====")

print(region_summary)

best_region = region_summary["Total_Profit"].idxmax()

print("\nBest Region by Profit:", best_region)

best_region_profit = region_summary.loc[
    best_region,
    "Total_Profit"
]

print(f"Profit: ${best_region_profit:,.2f}")

high_margin_products = sales[
    sales["Profit_Margin"] > 40
]

print("\n===== HIGH MARGIN PRODUCTS =====")

print(
    high_margin_products[
        ["Product", "Profit", "Profit_Margin"]
    ]
)

top_3 = sales.sort_values(
    "Profit",
    ascending=False
).head(3)


print("\n===== TOP 3 PRODUCTS =====")

print(
    top_3[
        ["Product", "Revenue", "Profit"]
    ]
)

sales.to_csv(
    "cleaned_business_sales.csv",
    index=False
)