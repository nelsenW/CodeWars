def is_vow(inp):
    vowels = "aeiou"
    ans = []
    for num in inp:
        if chr(num) in vowels:
            ans.append(chr(num))
        else: 
            ans.append(num)
    return ans