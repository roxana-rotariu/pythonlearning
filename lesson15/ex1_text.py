# Creează și scrie în fișier
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Salut!\n")
    file.write("Acesta este un fișier text.\n")
    file.write("Învățăm Python.\n")

# Citește fișierul linie cu linie
with open("hello.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
