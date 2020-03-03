import math
import random


def mean(X):
    return sum(X) / len(X)


def variance(X):
    X_mean = mean(X)

    actual_value = 0
    for X_i in X:
        actual_value += (X_i - X_mean) ** 2

    return actual_value / len(X)


def std(X):
    return math.sqrt(variance(X))


if __name__ == "__main__":
    data = [random.randint(0, 100) for _ in range(50)]

    print(f'Data: {data}')
    print(f'\tMean = {mean(data)}')
    print(f'\tVariance = {variance(data)}')
    print(f'\tStd = {std(data)}')
