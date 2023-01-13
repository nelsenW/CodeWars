def evil(n):
    result = 0
    txt = str(bin(n))
    for char in txt:
        if char == "1":
            result += 1
    
    return "It's Odious!" if result % 2 != 0 else "It's Evil!"