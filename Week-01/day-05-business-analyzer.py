import csv

def calculate_revenue(units,price):
    return units * price

def calculate_cost(units,cost_per_unit):
    return units * cost_per_unit

def calculate_profit(revenue,cost):
    return revenue - cost

def calculate_profit_margin(profit, revenue):
    return (profit/revenue) * 100

def print_sale_report(product, units, revenue, cost, profit, profit_margin):
    print(f"Product: {product}")
    print(f"Units: {units}")
    print(f"Revenue: ${revenue:,.2f}")
    print(f"Cost: ${cost:,.2f}")
    print(f"Profit: ${profit:,.2f}")
    print(f"Profit Margin: {profit_margin:.2f}%")

with open("sales.csv","r") as file:

    reader = csv.DictReader(file)

    total_revenue = 0
    total_cost = 0
    total_profit = 0

    for row in reader:

        product = row["Product"]
        units = int(row["Units"])
        price = float(row["Price"])
        cost_per_unit = float(row["Cost"])

        revenue = calculate_revenue(units,price)
        cost = calculate_cost(units,cost_per_unit)
        profit = calculate_profit(revenue,cost)
        profit_margin = calculate_profit_margin(profit,revenue)

        print_sale_report(product, units, revenue, cost, profit, profit_margin)
        print("-" * 40)

        total_revenue += revenue
        total_cost += cost
        total_profit += profit

    total_margin = (total_profit / total_revenue) * 100

    print("BUSINESS SUMMARY")
    print("=" * 40)
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Cost: ${total_cost:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Overall Margin: {total_margin:.2f}%")