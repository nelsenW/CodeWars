def sum_of_n(n):
    i = 1
    ans = [0]
    while len(ans) <= abs(n):
        ans.append((ans[i - 1] + i)) if n > 0 else ans.append((ans[i-1] - i))
        i+=1
    return ans