import time


def timmer(func):
    def wapplier(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} executed in {end-start} seconds")
        return result

    return wapplier


@timmer
def test(n):
    time.sleep(n)


test(2)
