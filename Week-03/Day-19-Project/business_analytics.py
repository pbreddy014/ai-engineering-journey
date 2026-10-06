import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def load_data(filename):

    print("Loading data...")

    sales = pd.read_csv(filename)

    print(f"Loaded {len(sales)} rows.")

    return sales

def validate_data(sales):

    required_columns = [
        "Product",
        "Units",
        "Price",
        "Cost",
        "Region"
    ]

    missing_columns = []

    for column in required_columns:

        if column not in sales.columns:
            missing_columns.append(column)

    if missing_columns:

        print("Validation failed.")
        print("Missing columns:", missing_columns)

        return False

    print("Validation successful.")

    return True

def data_quality_report(sales):

    print("\n===== DATA QUALITY REPORT =====")

    print(f"Rows: {sales.shape[0]}")
    print(f"Columns: {sales.shape[1]}")

    print("\nMissing Values:")
    print(sales.isnull().sum())

    print("\nDuplicate Rows:")
    print(sales.duplicated().sum())

def clean_data(sales):

    print("\nCleaning data...")

    original_rows = len(sales)

    sales = sales.drop_duplicates()

    sales = sales.dropna(
        subset=[
            "Product",
            "Units",
            "Price",
            "Cost"
        ]
    )

    sales["Region"] = sales["Region"].fillna(
        "Unknown"
    )

    sales["Region"] = sales["Region"].replace({
        "United States": "USA",
        "U.S.A.": "USA",
        "United Kingdom": "UK",
        "U.K.": "UK"
    })

    cleaned_rows = len(sales)

    print(
        f"Rows removed: "
        f"{original_rows - cleaned_rows}"
    )

    return sales

def remove_invalid_values(sales):

    sales = sales[
        (sales["Units"] >= 0)
        & (sales["Price"] >= 0)
        & (sales["Cost"] >= 0)
    ]

    return sales


def create_features(sales):

    print("Creating business features...")

    sales["Revenue"] = (
        sales["Units"] * sales["Price"]
    )

    sales["Total_Cost"] = (
        sales["Units"] * sales["Cost"]
    )

    sales["Profit"] = (
        sales["Revenue"]
        - sales["Total_Cost"]
    )

    sales["Profit_Margin"] = 0.0

    sales.loc[
        sales["Revenue"] > 0,
        "Profit_Margin"
    ] = (
        sales["Profit"]
        / sales["Revenue"]
        * 100
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

def calculate_kpis(sales):

    total_revenue = sales["Revenue"].sum()
    total_cost = sales["Total_Cost"].sum()
    total_profit = sales["Profit"].sum()

    average_profit = sales["Profit"].mean()

    overall_margin = (
        total_profit / total_revenue * 100
    )

    return {
        "Total Revenue": total_revenue,
        "Total Cost": total_cost,
        "Total Profit": total_profit,
        "Average Profit": average_profit,
        "Overall Margin": overall_margin
    }


def print_kpis(kpis):

    print("\n===== EXECUTIVE KPI SUMMARY =====")

    print(
        f"Total Revenue: "
        f"${kpis['Total Revenue']:,.2f}"
    )

    print(
        f"Total Cost: "
        f"${kpis['Total Cost']:,.2f}"
    )

    print(
        f"Total Profit: "
        f"${kpis['Total Profit']:,.2f}"
    )

    print(
        f"Average Profit: "
        f"${kpis['Average Profit']:,.2f}"
    )

    print(
        f"Overall Margin: "
        f"{kpis['Overall Margin']:.2f}%"
    )

def create_region_summary(sales):

    summary = sales.groupby("Region").agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Cost=("Total_Cost", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean"),
        Product_Count=("Product", "count")
    )

    summary = summary.reset_index()

    summary = summary.sort_values(
        "Total_Profit",
        ascending=False
    )

    return summary


def create_product_summary(sales):

    summary = sales[
        [
            "Product",
            "Region",
            "Revenue",
            "Profit",
            "Profit_Margin"
        ]
    ]

    summary = summary.sort_values(
        "Profit",
        ascending=False
    )

    return summary

def perform_eda(sales):

    print("\n===== EXPLORATORY DATA ANALYSIS =====")

    print("\nRevenue Statistics:")
    print(sales["Revenue"].describe())

    print("\nProfit Statistics:")
    print(sales["Profit"].describe())

    print("\nMean Profit:")
    print(sales["Profit"].mean())

    print("\nMedian Profit:")
    print(sales["Profit"].median())

    correlation = sales["Revenue"].corr(
        sales["Profit"]
    )

    print(
        "\nRevenue vs Profit Correlation:",
        round(correlation, 2)
    )

def create_profit_chart(sales):

    ranking = sales.sort_values(
        "Profit",
        ascending=True
    )

    plt.figure()

    plt.barh(
        ranking["Product"],
        ranking["Profit"]
    )

    plt.title("Profit by Product")
    plt.xlabel("Profit")
    plt.ylabel("Product")

    plt.tight_layout()

    plt.savefig(
        "charts/profit-by-product.png"
    )

    plt.close()

def create_region_chart(region_summary):

    plt.figure()

    plt.bar(
        region_summary["Region"],
        region_summary["Total_Revenue"]
    )

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.savefig(
        "charts/revenue-by-region.png"
    )

    plt.close()

def create_correlation_chart(sales):

    plt.figure()

    plt.scatter(
        sales["Revenue"],
        sales["Profit"]
    )

    plt.title("Revenue vs Profit")
    plt.xlabel("Revenue")
    plt.ylabel("Profit")

    plt.tight_layout()

    plt.savefig(
        "charts/revenue-vs-profit.png"
    )

    plt.close()



def export_reports(
    sales,
    region_summary,
    product_summary
):

    sales.to_csv(
        "output/cleaned-sales.csv",
        index=False
    )

    region_summary.to_csv(
        "output/region-summary.csv",
        index=False
    )

    product_summary.to_csv(
        "output/product-summary.csv",
        index=False
    )

def create_output_folders():

    Path("charts").mkdir(exist_ok=True)
    Path("output").mkdir(exist_ok=True)

def main():

    create_output_folders()

    sales = load_data(
        "business_sales.csv"
    )

    if not validate_data(sales):
        print("Pipeline stopped.")
        return

    data_quality_report(sales)

    sales = clean_data(sales)

    sales = remove_invalid_values(sales)

    sales = create_features(sales)

    kpis = calculate_kpis(sales)

    print_kpis(kpis)

    region_summary = create_region_summary(
        sales
    )

    product_summary = create_product_summary(
        sales
    )

    perform_eda(sales)

    create_profit_chart(sales)

    create_region_chart(
        region_summary
    )

    create_correlation_chart(sales)

    export_reports(
        sales,
        region_summary,
        product_summary
    )

    print("\nAnalytics pipeline completed!")


if __name__ == "__main__":
    main()