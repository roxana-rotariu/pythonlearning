# Creează fișier mare cu 10000 linii
with open("bigfile.txt", "w", encoding="utf-8") as file:
    for i in range(1, 10001):
        file.write(f"Linia {i}\n")

# Citește linie cu linie și numără
line_count = 0
with open("bigfile.txt", "r", encoding="utf-8") as file:
    for line in file:
        line_count += 1

print(f"Număr total de linii: {line_count}")
