import functools
def max_product(lst, n):
    lst.sort(reverse=True)
    ans = functools.reduce(lambda x,y: x * y,lst[:n], 1)
    return ans