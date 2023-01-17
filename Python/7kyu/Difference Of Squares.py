import functools
def difference_of_squares(n):
    a = sum(range(n+1)) ** 2 
    b = functools.reduce(lambda x, y: y ** 2 + x, range(n+1))
    return a - b