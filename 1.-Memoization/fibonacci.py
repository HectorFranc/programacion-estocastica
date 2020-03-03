import sys


def recursive_fibonacci(n):
    if n in [1, 2]:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def dynamic_fibonacci(n, _memoization_dict={}):
    if n in [1, 2]:
        return 1

    try:
        return _memoization_dict[n]
    except KeyError:
        result = dynamic_fibonacci(n - 1, _memoization_dict) + dynamic_fibonacci(n - 2, _memoization_dict)
        _memoization_dict[n] = result
        return result


if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    fibo_num = int(input('Fibonacci number\n>> '))
    print(dynamic_fibonacci(fibo_num))
