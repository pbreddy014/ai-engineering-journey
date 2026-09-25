sales = [1200, 1500, 900, 1800, 2100, 1350, 1750]

threshold = 1500

for sale in sales:
    if sale > threshold:
        print(f"${sale:,.2f}")


salespeople = [
    "John",
    "Sarah",
    "Mike",
    "Lisa",
    "David",
    "Priya",
    "Raj"
]

for sale in sales:
    print(f"{salespeople[sales.index(sale)]} -> ${sale:,.2f}")

for position, sale in enumerate(sales):
    print(position,sale)

for number in range(1,11,1):
    print(f"{number}")

number = 10
while number > 0:
    print(f"{number}")
    number -= 1


while True:
    number = int(input("enter a positive number"))

    if number > 0:
        break