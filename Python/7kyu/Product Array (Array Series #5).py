import functools
def product_array(numbers):
    pro = functools.reduce(lambda x,y: x * y, numbers)
    return list(map(lambda x: pro/x, numbers))