import pandas as pd

sales = pd.read_csv("cleaned_business_sales.csv")

sales["Profit_Margin"] = (
    sales["Profit"] / sales["Revenue"] * 100
)

def revenue_category(revenue):

    if revenue >= 10000:
        return "High"

    elif revenue >= 5000:
        return "Medium"

    else:
        return "Low"

sales["Revenue_Category"] = sales["Revenue"].apply(
    revenue_category
)

sales["Profitable"] = sales["Profit"] > 0

sales["High_Value_Product"] = (
    sales["Revenue"] >= 10000
)

outliers = sales[
    sales["Units_Sold"] > 1000
]

def sales_volume_category(units):

    if units >= 50:
        return "High"

    elif units >= 20:
        return "Medium"

    else:
        return "Low"


sales["Sales_Volume_Category"] = sales[
    "Units_Sold"
].apply(sales_volume_category)

sales["Cost_Percentage"] = (
    sales["Total_Cost"] / sales["Revenue"] * 100
)

prepared_data = sales[
    [
        "Product",
        "Region",
        "Units_Sold",
        "Unit_Price",
        "Unit_Cost",
        "Revenue",
        "Total_Cost",
        "Profit",
        "Profit_Margin",
        "Revenue_Category",
        "Profitable",
        "Sales_Volume_Category",
        "Cost_Percentage"
    ]
]

prepared_data.to_csv(
    "prepared_business_sales.csv",
    index=False
)

ml_features = sales[
    [
        "Units_Sold",
        "Unit_Price",
        "Unit_Cost",
        "Revenue",
        "Profit",
        "Profit_Margin"
    ]
]

ml_features.to_csv(
    "ml_features.csv",
    index=False
)