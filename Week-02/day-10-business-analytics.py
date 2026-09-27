import csv

def load_sales_data(filename):

    sales = []

    with open(filename,"r") as file:

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


def calculate_revenue(sale):

    return sale["units"] * sale["price"]


def calculate_cost(sale):

    return sale["units"] * sale["cost"]


def calculate_profit(sale):

    revenue = calculate_revenue(sale)
    cost = calculate_cost(sale)

    return revenue - cost


def calculate_margin(sale):

    revenue = calculate_revenue(sale)
    profit = calculate_profit(sale)

    return (profit / revenue) * 100


def business_summary(sales):

    total_units = 0
    total_revenue = 0
    total_cost = 0
    total_profit = 0

    for sale in sales:

        total_units += sale["units"]
        total_revenue += calculate_revenue(sale)
        total_cost += calculate_cost(sale)
        total_profit += calculate_profit(sale)

    margin = (total_profit / total_revenue) * 100

    print()
    print("=" * 40)
    print("BUSINESS SUMMARY")
    print("=" * 40)

    print(f"Total Units: {total_units:,}")
    print(f"Revenue: ${total_revenue:,.2f}")
    print(f"Cost: ${total_cost:,.2f}")
    print(f"Profit: ${total_profit:,.2f}")
    print(f"Margin: {margin:.2f}%")

    print("=" * 40)


def show_top_products(sales):

    ranked_sales = sorted(
        sales,
        key=lambda sale: calculate_profit(sale),
        reverse=True
    )

    print()
    print("=" * 40)
    print("TOP PRODUCTS")
    print("=" * 40)

    for sale in ranked_sales[:3]:

        profit = calculate_profit(sale)

        print(
            f"{sale['product']:<15}"
            f"${profit:>12,.2f}"
        )

    print("=" * 40)

def region_analysis(sales):

    region = input("Enter region: ").strip()

    total_revenue = 0
    total_profit = 0

    found = False

    for sale in sales:

        if sale["region"].lower() == region.lower():

            found = True

            total_revenue += calculate_revenue(sale)
            total_profit += calculate_profit(sale)

    if not found:

        print()
        print("Region not found.")
        return

    print()
    print("=" * 40)
    print(f"REGION ANALYSIS: {region}")
    print("=" * 40)

    print(f"Revenue: ${total_revenue:,.2f}")
    print(f"Profit: ${total_profit:,.2f}")

    print("=" * 40)

def show_high_profit_products(sales):

    try:

        threshold = float(
            input("Enter minimum profit: ")
        )

    except ValueError:

        print("Please enter a valid number.")
        return

    print()
    print("=" * 40)
    print("HIGH PROFIT PRODUCTS")
    print("=" * 40)

    found = False

    for sale in sales:

        profit = calculate_profit(sale)

        if profit >= threshold:

            found = True

            print(
                f"{sale['product']:<15}"
                f"${profit:>12,.2f}"
            )

    if not found:

        print("No products found.")

    print("=" * 40)

def show_lowest_profit_product(sales):

    lowest_profit = float("inf")

    for sale in sales:
        profit = calculate_profit(sale)

        if profit < lowest_profit:
            lowest_profit_product = sale
            lowest_profit = profit

    print()
    print("=" * 40)
    print("LOWEST PROFIT PRODUCT")
    print("=" * 40)

    print(
        f"{lowest_profit_product['product']:<15}"
        f"${lowest_profit:>12,.2f}"
    )

    print("=" * 40)

def search_product(sales):

    product = input("Enter product name: ").strip()
    found = False
    found_product = ""

    for sale in sales:
        
        if sale['product'].lower() == product.lower():
            found_product = sale
            found = True
            break
        
    if found:
        print()
        print("=" * 40)
        print("FOUND PRODUCT")
        print("-" * 30)
        print(found_product)
        print("=" * 40)

    if not found:
        print()
        print("=" * 40)
        print(f"{product} NOT FOUND PRODUCT")
        print("=" * 40)

    print("=" * 40)

def show_menu():

    print()
    print("=" * 40)
    print("BUSINESS SALES ANALYTICS")
    print("=" * 40)

    print("1. Business Summary")
    print("2. Top Products")
    print("3. Region Analysis")
    print("4. High Profit Products")
    print("5. Lowest Profit Product")
    print("6. Search Product")
    print("7. Exit")

    print("=" * 40)

sales = load_sales_data("business_sales.csv")


while True:

    show_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        business_summary(sales)

    elif choice == "2":

        show_top_products(sales)

    elif choice == "3":

        region_analysis(sales)

    elif choice == "4":

        show_high_profit_products(sales)

    elif choice == "5":

        show_lowest_profit_product(sales)
    
    elif choice == "6":

        search_product(sales)

    elif choice == "7":

        print("Thank you for using Business Sales Analytics.")
        break

    else:

        print("Invalid choice. Please select 1-5.")