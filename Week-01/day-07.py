import csv

def calculate_achievement(sales,target):
    return (sales / target) * 100

print(f"=" * 50)
print("Employee Performance Analyzer")
print(f"=" * 50)

print("\nIndividual performance\n")


with open("employee_performance.csv", "r") as file:

    reader = csv.DictReader(file)

    total_sales = 0
    total_target = 0
    total_customers = 0
    employee_count = 0

    highest_sales = 0
    highest_sales_person = ""

    lowest_sales = float("inf")
    lowest_sales_person = ""

    highest_cutomers = 0
    
    above_target = []

    employee_results = []

    for row in reader:

        employee_name = row["Employee"]
        department = row["Department"]
        sales = float(row["Sales"])
        target = float(row["Target"])
        customers = int(row["Customers"])
        achievement = calculate_achievement(sales,target)
    
        employee_results.append({
            "employee": employee_name,
            "department": department,
            "sales": sales,
            "target": target,
            "achievement": achievement,
            "customers": customers
        })



        total_sales += sales
        total_target += target
        total_customers += customers
        employee_count += 1

        #Highest Sales
        if sales > highest_sales:
            highest_sales = sales
            highest_sales_person = employee_name

        #Lowest Sales
        if sales <= lowest_sales:
            lowest_sales = sales
            lowest_sales_person = employee_name

        if achievement > 100:
            above_target.append(employee_name)

        if customers > highest_cutomers:
            highest_cutomers = customers

    total_achievement = calculate_achievement(total_sales,total_target)
    average_sales = total_sales / employee_count
    average_customers = total_customers / employee_count

    print("\nOverall Performance\n")

    print(f"Total Number of Employees: {employee_count}")
    print(f"Total Sales: ${total_sales:,}")
    print(f"Total Target: ${total_target:,}")
    print(f"Overall Achievement Percentage: {total_achievement:,.2f}%")
    print(f"Customers: {total_customers:,}\n")

    print(f"Highest Salesperson: {highest_sales_person}")
    print(f"Lowest Salesperson: {lowest_sales_person}\n")

    print("Above Target Employees")
    for employee in above_target:
        print(employee)

    print(f"\nAverage Sales: ${average_sales:,.2f}")
    print(f"\nHighest Number of Customers: {highest_cutomers}")

    print("\nIndividual Performance\n")

    for emp in employee_results:
        print(f"Employee: {emp["employee"]}")
        print(f"Department: {emp["department"]}")
        print(f"Sales: ${emp["sales"]:,}")
        print(f"Target: ${emp["target"]:,}")
        print(f"Achievement %: {emp["achievement"]:,.2f}%")
        print(f"Customers: {emp["customers"]}\n")
    