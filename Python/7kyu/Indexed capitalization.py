def capitalize(s,ind):
    ans = []
    for idx, char in enumerate(s):
        if idx in ind:
            ans.append(char.upper())
        else:
            ans.append(char)
    return "".join(ans)