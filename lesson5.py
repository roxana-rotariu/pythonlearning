from dataclasses import dataclass
from typing import Protocol
import json


# -------------------------------
# Rectangle with @property
# -------------------------------
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


# -------------------------------
# MathTools with static methods
# -------------------------------
class MathTools:
    @staticmethod
    def is_positive(n):
        return n > 0

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except:
            return False


# -------------------------------
# JSON Mixin
# -------------------------------
class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

    def from_json(self, data: str):
        values = json.loads(data)
        self.__dict__.update(values)


# -------------------------------
# User with classmethod + mixin
# -------------------------------
class User(JsonMixin):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first, last = full_name.split()
        return cls(first, last)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return (
            f"User(first_name='{self.first_name}', "
            f"last_name='{self.last_name}')"
        )


# -------------------------------
# Dataclass immutabil
# -------------------------------
@dataclass(frozen=True)
class Point:
    x: int
    y: int


# -------------------------------
# Serializer Protocol
# -------------------------------
class Serializer(Protocol):
    def to_json(self) -> str: ...


# -------------------------------
# User and Product Serializers
# -------------------------------
class UserSerializer:
    @staticmethod
    def save(obj: Serializer):
        print(obj.to_json())


class ProductSerializer:
    @staticmethod
    def save(obj: Serializer):
        print(obj.to_json())

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __eq__(self, value):
        return isinstance(value, Product) and self.name == value.name and self.price == value.price
    def __lt__(self, other):
        return self.price < other.price
    
# -------------------------------
# Demo
# -------------------------------
if __name__ == "__main__":
    r = Rectangle(10, 20)
    print(r.area)
    print(r.perimeter)

    print(MathTools.is_positive(10))
    print(MathTools.is_even(10))
    print(MathTools.is_float("mm"))
    print(MathTools.is_float(10.5))

    u = User.from_full_name("John Doe")
    print(u.to_json())
    print(u)

    u2 = User("Jane", "Doe")
    print(u2.to_json())
    u2.from_json('{"first_name": "Janet", "last_name": "Smith"}')
    print(u2.to_json())

    p1 = Point(10, 10)
    print(p1)

    # Now fully valid — User respects Serializer (to_json exists)
    UserSerializer.save(u2)
    ProductSerializer.save(u2)
    
    p = Product("Book", 10)
    p2 = Product("Book", 15)
    print(p == p2)
    print(p < p2)