def string_transformer(s):
    ans = []
    words = s.split(" ")
    for word in words:
        reverse = []
        for char in word:
            if char.islower():
                reverse.append(char.upper())
            else:
                reverse.append(char.lower())
        ans.append("".join(reverse))
        
    ans.reverse()
    return " ".join(ans)