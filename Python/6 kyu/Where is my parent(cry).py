def find_children(p):
    p = list(p)
    p.sort(key= lambda x: (x.lower(), ord(x))) 
    return "".join(p)