def multiples(m, n):
    i = 1
    ans = []
    while i <= m:
        ans.append(n * i)
        i += 1
    return ans