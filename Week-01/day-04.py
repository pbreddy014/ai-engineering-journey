sales = [
    {
        "product": "Laptop",
        "units": 10,
        "price": 1200,
        "cost": 800
    },
    {
        "product": "Monitor",
        "units": 20,
        "price": 400,
        "cost": 250
    },
    {
        "product": "Keyboard",
        "units": 50,
        "price": 80,
        "cost": 40
    }
]

def calculate_revenue(units,price):
    return units * price

def calculate_cost(units,cost):
    return units * cost

def calculate_profit(total_revenue,total_cost):
    return total_revenue - total_cost

def calculate_profit_margin(total_revenue,total_profit):
    return (total_profit / total_revenue) * 100

final_revenue = 0

for sale in sales:
    #revenue = calculate_revenue(sale["units"],sale["price"])

    revenue = calculate_revenue(sale["units"],sale["price"])
    cost = calculate_cost(sale["units"],sale["cost"])
    profit = calculate_profit(revenue,cost)
    profit_margin = calculate_profit_margin(revenue,profit)

    print(f"Product: {sale["product"]}")
    print(f"Units: {sale["units"]}")
    print(f"Revenue: {revenue}")
    print(f"Cost: {cost}")
    print(f"Profit: {profit}")
    print(f"Margin: {profit_margin}\n")
   # print(f"Revenue {revenue}")

    final_revenue += revenue

print(f"Total Revenue : {final_revenue}")