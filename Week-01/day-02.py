
def get_positive_integer(promt):
    while True:
        try:
            value =  int(input(promt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


units_sold = get_positive_integer("Enter units sold: ")
price_per_unit = get_float("Enter price per unit: ")
cost_per_unit = get_float("Enter cost per unit: ")

revenue = units_sold * price_per_unit
total_cost = units_sold * cost_per_unit
profit = revenue - total_cost
profit_margin = (profit / revenue) * 100

print("---- BUSINESS KPI REPORT ----\n\n")

print(f"Units Sold: {units_sold:,}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Total Cost: ${total_cost:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {profit_margin:,.2f}%")