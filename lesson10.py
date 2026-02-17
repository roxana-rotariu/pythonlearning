# lesson10.py

from functools import reduce, partial, lru_cache
from operator import mul


# ✔ Exercițiul 1 — map
def square_all(nums):
    return list(map(lambda x: x ** 2, nums))


# ✔ Exercițiul 2 — filter
def remove_negatives(nums):
    return list(filter(lambda x: x >= 0, nums))


# ✔ Exercițiul 3 — reduce
def product(nums):
    return reduce(mul, nums, 1)


# ✔ Exercițiul 4 — partial
# pow(base, exp)
power_of_3 = partial(pow, exp=3)
# Alternativ corect (mai explicit):
# power_of_3 = lambda x: pow(x, 3)


# ✔ Exercițiul 5 — lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ✔ Exercițiul 6 — Functional pipeline (o singură linie)
def pipeline(nums):
    return sum(
        map(
            lambda x: x ** 2,
            map(
                lambda x: x * 2,
                filter(lambda x: x > 0, nums)
            )
        )
    )


# Exemplu de test
if __name__ == "__main__":
    nums = [-3, -1, 0, 2, 4]

    print(square_all(nums))        # [9, 1, 0, 4, 16]
    print(remove_negatives(nums))  # [0, 2, 4]
    print(product([1, 2, 3, 4]))   # 24
    print(power_of_3(2))           # 8
    print(fibonacci(10))           # 55
    print(pipeline(nums))          # 80
