from functools import reduce


def my_func(a, b ):
    return a*b


ls = [i for i in range(100,1001) if i%2 == 0]
print(reduce(my_func, ls))