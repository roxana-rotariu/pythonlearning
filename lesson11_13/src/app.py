from models.product import Product

product = Product("Laptop", 1200)
product.apply_discount(10)  # reducere 10%
print(f"Price after discount: ${product.price}")