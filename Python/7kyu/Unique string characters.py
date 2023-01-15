def solve(a,b):
    ans = []
    
    for char in a:
        if char not in b:
            ans.append(char)
            
    for char in b:
        if char not in a:
            ans.append(char)
            
    return ''.join(ans)