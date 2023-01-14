def tidyNumber(n):
    i = 0
    s = str(n)
    while i < len(s) - 1:
        if s[i] > s[i + 1]:
            return False
        i += 1
    return True