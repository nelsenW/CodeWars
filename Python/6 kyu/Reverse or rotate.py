def rev_rot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ""
    chunks = []
    
    while len(strng) >= sz:
        chunks.append(strng[:sz])
        strng = strng[sz:]
    ans = []  
    
    for chunk in chunks:
        tot = 0
        for char in chunk:
            tot += int(char) ** 3

        if tot % 2 == 0:
            ans.append(chunk[::-1])
        else:
            ans.append(chunk[1:] + chunk[:1])

    
    return "".join(ans)
    