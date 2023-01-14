def last(s):
    s = s.split()
    s.sort(key= lambda x: x[-1])
    return s

