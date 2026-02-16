class Product:
    def __init__(self, name: str, price: float, stock: int = 0):
        self.name = name
        self.price = price
        self.stock = stock
        
    def is_available(self) -> bool:
        return self.stock > 0
    
    def __str__(self) -> str:
        status = "In stock" if self.is_available() else "Out of stock"
        return f"{self.name}: ${self.price} ({status})"


class Store:
    def __init__(self, products: list[Product]):
        self.products = products

    def get_available_products(self) -> list[Product]:
        return [p for p in self.products if p.is_available()]
    
    def get_cheapest_products(self, n: int = 3) -> list[Product]:
        return sorted(self.products, key=lambda p: p.price)[:n]
    
    def search(self, query: str) -> list[Product]:
        q = query.lower()
        return [p for p in self.products if q in p.name.lower()]
    
    def total_stock_value(self) -> float:
        return sum(p.price * p.stock for p in self.products)
      
if __name__ == "__main__":
    products = [
        Product("Laptop", 1000, 5),
        Product("Smartphone", 500, 10),
        Product("Tablet", 300, 0),
        Product("Headphones", 100, 15),
        Product("Smartwatch", 200, 8),
    ]
    store = Store(products)

    print("Available products:")
    for product in store.get_available_products():
        print(product)

    print("\nCheapest products:")
    for product in store.get_cheapest_products(1):
        print(product)

    print("\nSearch results for 'smart':")
    for product in store.search("smart"):
        print(product)

    print(f"\nTotal stock value: ${store.total_stock_value()}")
