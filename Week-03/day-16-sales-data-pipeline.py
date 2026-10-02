import pandas as pd

def load_data(filename):

    print("Loading data...")

    sales = pd.read_csv(filename)

    return sales

def validate_data(sales):

    required_columns = [
        "Product",
        "Units",
        "Price",
        "Cost",
        "Region"
    ]

    for column in required_columns:

        if column not in sales.columns:
            print(f"Missing column: {column}")
            return False

    return True


def clean_data(sales):

    sales = sales.drop_duplicates()

    sales = sales.dropna(
        subset=["Product", "Units", "Price", "Cost"]
    )

    sales["Region"] = sales["Region"].fillna("Unknown")

    sales["Region"] = sales["Region"].replace({
        "U.K.": "UK",
        "United Kingdom": "UK",
        "United States": "USA",
        "U.S.A.": "USA"
    })

    return sales


def create_features(sales):

    print("Creating features...")

    sales["Revenue"] = (
        sales["Units"] * sales["Price"]
    )

    sales["Total_Cost"] = (
        sales["Units"] * sales["Cost"]
    )

    sales["Profit"] = (
        sales["Revenue"] - sales["Total_Cost"]
    )

    sales["Profit_Margin"] = (
        sales["Profit"] / sales["Revenue"] * 100
    )

    sales["Profit_Category"] = (
    sales["Profit"].apply(classify_profit)
    )

    return sales

def classify_profit(profit):

    if profit >= 5000:
        return "High"

    elif profit >= 2000:
        return "Medium"

    else:
        return "Low"


def create_region_summary(sales):

    region_summary = sales.groupby("Region").agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Cost=("Total_Cost", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean"),
        Product_Count=("Product", "count")
    )

    region_summary = region_summary.reset_index()

    region_summary = region_summary.sort_values(
        "Total_Profit",
        ascending=False
    )

    return region_summary


def print_business_summary(sales):

    total_revenue = sales["Revenue"].sum()
    total_cost = sales["Total_Cost"].sum()
    total_profit = sales["Profit"].sum()

    overall_margin = (
        total_profit / total_revenue * 100
    )

    print("\n===== BUSINESS SUMMARY =====")

    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Cost: ${total_cost:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Overall Margin: {overall_margin:.2f}%")

 
def export_data(sales, region_summary):

    print("\nExporting reports...")

    sales.to_csv(
        "day-16-prepared-sales.csv",
        index=False
    )

    region_summary.to_csv(
        "day-16-region-summary.csv",
        index=False
    )    



def create_product_summary(sales):

    product_summary = sales[
        ["Product", "Revenue", "Profit", "Profit_Margin"]
    ]
    
    product_summary = product_summary.sort_values(
        "Profit",
        ascending=False
    )

    return product_summary


def find_best_product(sales):
    return sales.loc[sales["Profit"].idxmax()]


def main():

    sales = load_data("business_sales.csv")

    if validate_data(sales):

        sales = clean_data(sales)

        sales = create_features(sales)

        region_summary = create_region_summary(sales)

        product_summary = create_product_summary(sales)

        best_product = find_best_product(sales)

        print_business_summary(sales)

        print("\n===== REGION SUMMARY =====")
        print(region_summary)

        print("\n===== PRODUCT SUMMARY =====")
        print(product_summary)    

        print("\n===== BEST PRODUCT =====")
        print(best_product)

        export_data(sales, region_summary)

        print("\nPipeline completed successfully.")

    else:

        print("Pipeline stopped because validation failed.")


if __name__ == "__main__":
    main()


