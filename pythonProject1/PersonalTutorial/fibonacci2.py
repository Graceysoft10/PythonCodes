_cache = {}


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 1:
        raise ValueError("should be positive")
    elif type(n) != int:
        raise TypeError("Should be an integer")
    if n in _cache:
        return _cache[n]
    else:
        result = fib(n - 1) + fib(n - 2)
        _cache[n] = result
        return result


for i in range(1, 11):
    print(fib(i))
