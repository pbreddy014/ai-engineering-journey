import pandas as pd

sales = pd.read_csv("business_sales.csv")

sales["Revenue"] = sales["Units"] * sales["Price"]
sales["Total Cost"] = sales["Units"] * sales["Cost"]
sales["Profit"] = sales["Revenue"] - sales["Total Cost"]

sales["Profit Margin"] = (
    sales["Profit"] /
    sales["Revenue"] *
    100
)

total_revenue = sales["Revenue"].sum()

total_cost = sales["Total Cost"].sum()

total_profit = sales["Profit"].sum()


print(f"Revenue: ${total_revenue:,.2f}")
print(f"Cost: ${total_cost:,.2f}")
print(f"Profit: ${total_profit:,.2f}")

overall_margin = (
    total_profit /
    total_revenue *
    100
)

print(f"Margin: {overall_margin:.2f}%")

best_product = sales.loc[
    sales["Profit"].idxmax()
]

print(best_product)

ranked = sales.sort_values("Profit",ascending=False)
print(ranked)

print(
    sales[
        ["Product","Region","Profit"]
    ]
)


print(
    sales[
        sales["Profit"] > 2000
    ]
)

print(sales["Profit"].mean())

high_margin = sales[
    sales["Profit Margin"] > 30
]

print(high_margin)

print(sales.groupby("Region")["Revenue"].sum())