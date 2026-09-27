import csv


def load_sales_data(filename):

    sales = []

    with open(filename, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            sales.append(row)

    return sales

def calculate_revenue(units, price):
    return units * price


def calculate_cost(units, cost):
    return units * cost


def calculate_profit(revenue, cost):
    return revenue - cost


def calculate_margin(profit, revenue):
    return (profit / revenue) * 100

def calculate_summary(sales):

    total_units = 0
    total_revenue = 0
    total_cost = 0
    total_profit = 0

    for row in sales:

        units = int(row["Units"])
        price = float(row["Price"])
        cost = float(row["Cost"])

        revenue = calculate_revenue(units, price)
        product_cost = calculate_cost(units, cost)
        profit = calculate_profit(revenue, product_cost)

        total_units += units
        total_revenue += revenue
        total_cost += product_cost
        total_profit += profit

    margin = calculate_margin(total_profit, total_revenue)

    return total_units, total_revenue, total_cost, total_profit, margin

def print_summary(total_units, revenue, cost, profit, margin):

    print()
    print("=" * 40)
    print("BUSINESS SALES SUMMARY")
    print("=" * 40)

    print(f"Total Units: {total_units:,}")
    print(f"Revenue: ${revenue:,.2f}")
    print(f"Cost: ${cost:,.2f}")
    print(f"Profit: ${profit:,.2f}")
    print(f"Profit Margin: {margin:.2f}%")

    print("=" * 40)

def find_best_product(sales):

    best_product = ""
    highest_profit = 0

    for row in sales:

        product = row["Product"]

        units = int(row["Units"])
        price = float(row["Price"])
        cost = float(row["Cost"])

        revenue = calculate_revenue(units, price)
        product_cost = calculate_cost(units, cost)
        profit = calculate_profit(revenue, product_cost)

        if profit > highest_profit:
            highest_profit = profit
            best_product = product

    return best_product, highest_profit

def find_lowest_profit(sales):

    lowest_product = ""
    lowest_profit = float("inf")

    for row in sales:

        product = row["Product"]

        units = int(row["Units"])
        price = float(row["Price"])
        cost = float(row["Cost"])

        revenue = calculate_revenue(units, price)
        product_cost = calculate_cost(units, cost)
        profit = calculate_profit(revenue, product_cost)

        if profit < lowest_profit:
            lowest_profit = profit
            lowest_product = product

    return lowest_product, lowest_profit



def find_high_profit_products(sales):

    high_profit_products = []

    for row in sales:

        product = row["Product"]

        units = int(row["Units"])
        price = float(row["Price"])
        cost = float(row["Cost"])

        revenue = calculate_revenue(units, price)
        product_cost = calculate_cost(units, cost)
        profit = calculate_profit(revenue, product_cost)

        if profit > 1000:
            high_profit_products.append(product)

    return high_profit_products



sales = load_sales_data("business_sales.csv")


print("=" * 50)
print("BUSINESS SALES ANALYTICS")
print("=" * 50)

print("1. Business Summary")
print("2. Best Product")
print("3. Lowest Product")
print("4. Products Above $1,000 Profit")
print("5. Exit\n")

choice = input("Enter your choice: ")

while True:
    if choice == "1":
        total_units, revenue, cost, profit, margin = calculate_summary(sales)
        print_summary(total_units, revenue, cost, profit, margin)
        break
    
    elif choice == "2":
        best_product, highest_profit = find_best_product(sales)

        print()
        print("TOP PRODUCT")
        print("-" * 40)
        print(f"Product: {best_product}")
        print(f"Profit: ${highest_profit:,.2f}")
        break
    elif choice == "3":
        worst_product, lowest_profit = find_lowest_profit(sales)

        print()
        print("LOWEST PROFIT")
        print("-" * 40)
        print(f"Product: {worst_product}")
        print(f"Profit: ${lowest_profit:,.2f}")
        break
    elif choice == "4":
        high_profit_products = find_high_profit_products(sales)
        print()
        print("HIGH PROFIT PRODUCTS")
        print("-" * 40)

        for product in high_profit_products:
            print(product)
        break
    elif choice == "5":
        break






