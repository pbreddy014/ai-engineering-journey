import csv

with open("sales.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)