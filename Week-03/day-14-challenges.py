import pandas as pd

sales = pd.read_csv("business_sales.csv")

sales["Revenue"] = sales["Units"] * sales["Price"]

highest_revenue_product = sales.loc[sales["Revenue"].idxmax()]

print(highest_revenue_product)