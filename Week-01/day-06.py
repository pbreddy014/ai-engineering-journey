import csv


def calculate_revenue(units, price):
    return units * price


def calculate_cost(units, cost_per_unit):
    return units * cost_per_unit


def calculate_profit(revenue, cost):
    return revenue - cost


def calculate_profit_margin(profit, revenue):
    return (profit / revenue) * 100


total_units = 0
total_revenue = 0
total_cost = 0
total_profit = 0
product_count = 0

best_product = ""
highest_profit = 0


with open("business_sales.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        product = row["Product"]
        units = int(row["Units"])
        price = float(row["Price"])
        cost_per_unit = float(row["Cost"])
        region = row["Region"]

        revenue = calculate_revenue(units, price)
        cost = calculate_cost(units, cost_per_unit)
        profit = calculate_profit(revenue, cost)
        margin = calculate_profit_margin(profit, revenue)

        total_units += units
        total_revenue += revenue
        total_cost += cost
        total_profit += profit
        product_count += 1

        if profit > highest_profit:
            highest_profit = profit
            best_product = product

        print("-" * 40)
        print(f"Product: {product}")
        print(f"Region: {region}")
        print(f"Units Sold: {units}")
        print(f"Revenue: ${revenue:,.2f}")
        print(f"Cost: ${cost:,.2f}")
        print(f"Profit: ${profit:,.2f}")
        print(f"Profit Margin: {margin:.2f}%")


overall_margin = (total_profit / total_revenue) * 100


print()
print("=" * 40)
print("BUSINESS SUMMARY")
print("=" * 40)

print(f"Products Analyzed: {product_count}")
print(f"Total Units Sold: {total_units}")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Cost: ${total_cost:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Overall Profit Margin: {overall_margin:.2f}%")


print()
print("=" * 40)
print("TOP PERFORMER")
print("=" * 40)

print(f"Product: {best_product}")
print(f"Profit: ${highest_profit:,.2f}")