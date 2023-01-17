def beggars(values, n):
    if n < 1:
        return []
    ans = [0]*n
    i = 0
    for num in values:
        ans[i % n] += num
        i += 1 
    return ans