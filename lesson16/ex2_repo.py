import sqlite3
from dataclasses import dataclass
from typing import List, Optional


# Model (Entity)
@dataclass
class Product:
    id: Optional[int]
    name: str
    price: float


# Repository
class ProductRepository:
    def __init__(self, db_name: str = "products_repo.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """)
        self.conn.commit()

    def add(self, product: Product) -> Product:
        cursor = self.conn.execute(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            (product.name, product.price)
        )
        self.conn.commit()
        product.id = cursor.lastrowid
        return product

    def get(self, product_id: int) -> Optional[Product]:
        cursor = self.conn.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,)
        )
        row = cursor.fetchone()
        if row:
            return Product(id=row["id"], name=row["name"], price=row["price"])
        return None

    def list(self) -> List[Product]:
        cursor = self.conn.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        return [
            Product(id=row["id"], name=row["name"], price=row["price"])
            for row in rows
        ]

    def close(self):
        self.conn.close()


# --- Utilizare ---
if __name__ == "__main__":
    repo = ProductRepository()

    # Adăugăm produse
    repo.add(Product(id=None, name="Monitor", price=1200.0))
    repo.add(Product(id=None, name="Headphones", price=400.0))
    repo.add(Product(id=None, name="Webcam", price=250.0))

    # Listăm produsele
    products = repo.list()
    for p in products:
        print(p)

    repo.close()
