def rank(st, we, n):
    if not st:
        return "No participants"
    if n > len(we):
        return "Not enough participants"
    ans = {}
    for idx, name in enumerate(st.split(",")):
        total = 0
        for char in name.lower():
            total += ord(char) - 96
        total += len(name)
        ans[name] = total * we[idx]     
    
    ans = sorted(ans.items(), key=lambda x: (-x[1], x[0]))
    print(ans)
    return ans[n-1][0]
        
        