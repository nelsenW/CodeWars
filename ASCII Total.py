import functools

def uni_total(s):
    def convert(n):
        return ord(n)
    return 0 if len(s) == 0 else functools.reduce(lambda x, y: x+y, map(convert, s))