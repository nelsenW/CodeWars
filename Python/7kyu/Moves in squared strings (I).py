def vert_mirror(strng):
    s = strng.split()
    ans = []
    for let in s:
        x = list(let)
        x.reverse()
        ans.append("".join(x))
    return "\n".join(ans)
def hor_mirror(strng):
    s = strng.split()
    s.reverse()
    return "\n".join(s)
def oper(fct, s):
    return fct(s)