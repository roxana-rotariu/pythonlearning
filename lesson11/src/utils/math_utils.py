def add(a, b):
    return a + b

def percentage(value, percent):
    if percent < 0:
        raise ValueError("Percent cannot be negative")
    return value * (percent / 100)


def avg(nums):
    """Returnează media unei liste de numere."""
    if not nums:
        raise ValueError("List must not be empty")
    return sum(nums) / len(nums)