def pairs(ar):
    i = 0
    count = 0
    while i < len(ar) - 1:
        if(ar[i] == ar[i+1] - 1 or ar[i] == ar[i+1] + 1):
            count += 1
        i+=2
    return count