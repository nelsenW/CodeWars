import functools
def sum_triangular_numbers(n):
    if n < 1:
        return 0
    tri = [1]
    for num in range(2,n + 1):
        tri.append(num + tri[num - 2])
    return functools.reduce(lambda a,b: a + b, tri)