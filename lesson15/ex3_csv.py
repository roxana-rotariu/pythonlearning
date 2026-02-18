import csv

# Scriere în CSV
with open("people.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Roxana", 30])
    writer.writerow(["Alex", 25])
    writer.writerow(["Maria", 28])

# Citire cu DictReader
with open("people.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["age"]) > 26:
            print(row["name"])
