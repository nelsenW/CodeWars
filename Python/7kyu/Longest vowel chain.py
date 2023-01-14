def solve(s):
    longest = 0
    counter = 0 
    
    for char in s: 
        if char in ("a", "e", "i", "o", "u"):
            counter += 1
            if counter > longest:
                longest = counter
        else:
            counter = 0
    return longest

        