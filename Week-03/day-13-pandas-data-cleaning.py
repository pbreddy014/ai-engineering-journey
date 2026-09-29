import pandas as pd

#1 Load data
sales = pd.read_csv("business_sales.csv")

print("DATASET INFO")
print(sales.info())

print("\nMISSING VALUES")
print(sales.isnull().sum())

print("\nDUPLICATES")
print(sales.duplicated().sum())

sales.rename(columns={
    "Units" : "Units_Sold",
    "Price" : "Unit_Price"
})

sales["Region"] = sales["Region"].replace({
    "U.K." : "UK",
    "United Kingdom" : "UK"
})

sales = sales.drop_duplicates()

print("\nCLEANDED DATA")
print(sales)

print("\nFINAL DATA TYPES")
print(sales.dtypes)

print("\nFINAL MISSING VALUES")
print(sales.isnull().sum())