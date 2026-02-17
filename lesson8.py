def even_numbers(n):
    for x in range(n):
        if x % 2 == 0:
            yield x


def reverse_string(s):
    for char in reversed(s):
        yield char


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def read_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.rstrip("\n")


def read_numbers(filename):
    for line in read_lines(filename):
        yield int(line.strip())


def filter_positive(numbers):
    for num in numbers:
        if num > 0:
            yield num


def double(numbers):
    for num in numbers:
        yield num * 2


def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


if __name__ == "__main__":
    print(list(even_numbers(10)))
    print("".join(reverse_string("hello")))
    print(list(fibonacci(10)))
    
    print(list(read_lines("test.txt")))
    print(list(read_numbers("test.txt")))
    
    nums = [-1, 2, -3, 4, -5]
    print(list(filter_positive(nums)))
    
    print(list(double([1, 2, 3, 4, 5])))
    
    print(sum_numbers([1, 2, 3, 4, 5]))