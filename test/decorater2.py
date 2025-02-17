import time


def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def factorial(a, b):
    time.sleep(1)
    return a + b


print(factorial(10, 5))
