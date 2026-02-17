import time
from functools import wraps
import random


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, times + 1):
                try:
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Failed attempt {attempt}: {e}")
            raise last_exception
        return wrapper
    return decorator


@retry(3)
def unstable():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called with args={args}")
        return func(*args, **kwargs)
    return wrapper


def validate_types(*expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(
                    f"{func.__name__} expects {len(expected_types)} arguments"
                )
            for i, (arg, expected) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected):
                    raise TypeError(
                        f"Argument {i+1} must be {expected.__name__}, got {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_types(int, int)
def add(a, b):
    return a + b


print(add(2, 3))
slow_function()
print(unstable())