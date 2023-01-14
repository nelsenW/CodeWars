def squares(x, n):
    if n <= 0:
        return []
    i = 0
    ans = [x]
    while i < n - 1:
        x *= x
        ans.append(x)
        i += 1 
    return ans