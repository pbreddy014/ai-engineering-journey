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

plt.bar(
    profit_ranking["Product"],
    profit_ranking["Profit"]
)

plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "day-17-profit-by-product.png"
)

plt.show()