import psycopg2

# Config conexiune (modifică dacă este nevoie)
DB_CONFIG = {
    "dbname": "lesson16_db",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": 5432,
}

def main():
    # Conectare la PostgreSQL
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Creează tabel
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price NUMERIC(10,2) NOT NULL
    )
    """)

    # Inserează rânduri
    products = [
        ("Tablet", 2000.00),
        ("Speaker", 500.00),
        ("Microphone", 350.00)
    ]

    cursor.executemany(
        "INSERT INTO products (name, price) VALUES (%s, %s)",
        products
    )

    # Salvează modificările
    conn.commit()

    # Citește rândurile
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Închidere
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
