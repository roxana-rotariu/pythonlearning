import sqlite3

# Conectare (creează baza dacă nu există)
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Creează tabelul products
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

# Inserează 3 produse
products = [
    ("Laptop", 4500.0),
    ("Mouse", 150.0),
    ("Keyboard", 300.0)
]

cursor.executemany(
    "INSERT INTO products (name, price) VALUES (?, ?)",
    products
)

# Salvează modificările
conn.commit()

# Citește și afișează toate produsele
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Închide conexiunea
conn.close()
