def split_in_parts(s, l): 
    ans = []
    while len(s) > l:
        ans.append(s[:l])
        s = s[l:]
    return (" ".join(ans) + f' {s}').strip()