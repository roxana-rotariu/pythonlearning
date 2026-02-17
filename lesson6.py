from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
    
class ProductFactory:
    @staticmethod
    def create_basic(id, name, price, stock=10):
        return Product(id, name, price, stock)

    @staticmethod
    def create_premium(id, name, stock=5):
        return Product(id, name, price=99.99, stock=stock)
    
class TaxStrategy(ABC):
    @abstractmethod
    def calculate(self, price): ...

class NormalTax(TaxStrategy):
    def calculate(self, price):
        return price * 1.19    # TVA 19%

class ReducedTax(TaxStrategy):
    def calculate(self, price):
        return price * 1.09

class NoTax(TaxStrategy):
    def calculate(self, price):
        return price
    
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount): ...

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Crypto")
        
class ExternalInventoryAPI:
    def check(self, product_id):
        return product_id % 2 == 0  # even IDs = available
    
class InventoryAdapter:
    def __init__(self, external_api):
        self.external_api = external_api

    def is_in_stock(self, product):
        return self.external_api.check(product.id)
    
class LoggingDecorator:
    def __init__(self, component):
        self.component = component

    def pay(self, amount):
        print("[LOG] Starting payment...")
        result = self.component.pay(amount)
        print("[LOG] Payment finished.")
        return result
    
class ProductRepository(ABC):
    @abstractmethod
    def add(self, product): ...
    @abstractmethod
    def get(self, product_id): ...
    
class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product.id] = product

    def get(self, product_id):
        return self.products.get(product_id)
    
class Event:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, fn):
        self.subscribers.append(fn)

    def emit(self, data):
        for fn in self.subscribers:
            fn(data)
            
on_purchase = Event()
on_add_to_cart = Event()

class Config:
    _shared = {}

    def __init__(self, **kwargs):
        self.__dict__ = self._shared
        self.__dict__.update(kwargs)
        
class StoreFacade:
    def __init__(self, repository, tax_strategy, payment_strategy, inventory):
        self.repo = repository
        self.tax = tax_strategy
        self.pay = payment_strategy
        self.inventory = inventory

    def buy(self, product_id):
        product = self.repo.get(product_id)
        if not product:
            print("Product not found")
            return

        if not self.inventory.is_in_stock(product):
            print("Product out of stock (external check)")
            return

        price_with_tax = self.tax.calculate(product.price)

        print(f"Buying {product.name} for {price_with_tax:.2f}")
        self.pay.pay(price_with_tax)

        on_purchase.emit(product)
        
class StoreApp:
    def run(self):
        repo = InMemoryProductRepository()
        inventory = InventoryAdapter(ExternalInventoryAPI())

        # strategies
        tax = NormalTax()
        payment = LoggingDecorator(CardPayment())

        # products
        repo.add(ProductFactory.create_basic(1, "Laptop", 1200))
        repo.add(ProductFactory.create_basic(2, "Phone", 800))

        # facade
        store = StoreFacade(repo, tax, payment, inventory)

        # observers
        on_purchase.subscribe(lambda p: print(f"Event: Purchased {p.name}"))

        # try buying
        store.buy(1)
        store.buy(2)
        
app = StoreApp()
app.run()