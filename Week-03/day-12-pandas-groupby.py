import pandas as pd


sales = pd.read_csv("business_sales.csv")


sales["Revenue"] = sales["Units"] * sales["Price"]



sales["Total Cost"] = sales["Units"] * sales["Cost"]

sales["Profit"] = sales["Revenue"] - sales["Total Cost"]


region_summary = sales.groupby("Region").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Cost=("Total Cost", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Price=("Price", "mean"),
    Product_Count=("Product", "count")
)


best_region = region_summary.loc[
    region_summary["Total_Profit"].idxmax()
]

print(best_region)

region_revenue_summary = sales.groupby("Region")["Revenue"].sum()


region_profit = sales.groupby("Region")["Profit"].sum()

region_profit = (
    region_profit
    .reset_index()
    .sort_values("Profit",ascending=False)
)

print(region_profit)

region_revenue_summary = (
    region_revenue_summary
    .reset_index()
    .sort_values("Revenue",ascending=False)
)

print(region_revenue_summary)

region_summary = (
    region_summary
    .reset_index()
    .sort_values("Total_Profit", ascending=False)
)


print(region_summary)


print()
print("=" * 70)
print("REGIONAL BUSINESS REPORT")
print("=" * 70)

for _, row in region_summary.iterrows():

    print(
        f"{row['Region']:<10}"
        f"Revenue: ${row['Total_Revenue']:>12,.2f}   "
        f"Profit: ${row['Total_Profit']:>12,.2f}"
    )

print("=" * 70)

average_profit = sales.groupby("Region")["Profit"].mean()

print(average_profit)

best_region = average_profit.idxmax()
best_average_profit = average_profit.max()

print("Region with highest average profit:", best_region)
print("Average profit per product:", best_average_profit)
