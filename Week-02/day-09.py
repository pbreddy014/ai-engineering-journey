employees = [
    {"name": "Anita", "sales": 125000},
    {"name": "Rahul", "sales": 95000},
    {"name": "Priya", "sales": 140000}
]

sorted_employees = sorted(employees,key=lambda employee: employee["sales"],reverse=True)

for employee in sorted_employees:
    print(employee["name"], employee["sales"])