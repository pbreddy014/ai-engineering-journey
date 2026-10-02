import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("day-16-prepared-sales.csv")

profit_ranking = sales.sort_values(
    "Profit",
    ascending=False
)

region_profit = (
    sales.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

margin_ranking = sales.sort_values(
    "Profit_Margin",
    ascending=False
)

numeric_columns = sales[
    [
        "Units",
        "Price",
        "Cost",
        "Revenue",
        "Total_Cost",
        "Profit",
        "Profit_Margin"
    ]
]

correlation_matrix = numeric_columns.corr()

plt.figure()

plt.boxplot(
    sales["Profit"]
)

plt.title("Profit Box Plot")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()