import pandas as pd

sales = pd.read_csv("business_sales.csv")

india_sales = sales[
    sales["Region"] == "India"
    ]
print(india_sales)

sales["Revenue"] = ( sales["Units"] * sales["Price"]) 

print(sales)