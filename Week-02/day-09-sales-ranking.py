import csv


def load_sales_data(filename):

    sales = []

    with open(filename, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            sales.append({
                "product": row["Product"],
                "units": int(row["Units"]),
                "price": float(row["Price"]),
                "cost": float(row["Cost"]),
                "region": row["Region"]                
            })

    return sales

def calculate_profit(sale):
    revenue = sale["units"] * sale["price"]
    cost = sale["units"] * sale["cost"]

    return revenue - cost

def filter_by_region(sales,region):
    results = []

    for sale in sales:
        if sale["region"] == region:
            results.append(sale)
    return results

def filter_high_profit(sales,threshold):
    results = []

    for sale in sales:
        profit = calculate_profit(sale)

        if profit > threshold:
            results.append(sale)

    return results

def rank_by_profit(sales):
    return sorted(
        sales,
        key=lambda sale: calculate_profit(sale),
        reverse=True
    )

sales = load_sales_data("business_sales.csv")

ranked_sales = rank_by_profit(sales)

print()
print("=" * 40)
print("TOP 3 PRODUCTS BY PROFIT")
print("=" * 40)

top_three = sorted(ranked_sales[-3:], key=lambda sale: calculate_profit(sale))

for sale in top_three:
    profit = calculate_profit(sale)

    print(f"{sale["product"]}: ${profit:,.2f}")


india_sales = filter_by_region(sales,"India")
india_ranked = rank_by_profit(india_sales)

print()
print("=" * 40)
print("INDIA SALESs")
print("=" * 40)

for sale in india_ranked:
    profit = calculate_profit(sale)
    
    print(f"{sale["product"]}: ${profit:,.2f}")