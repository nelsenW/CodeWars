def count_deaf_rats(town):
    i = 0
    left = {
        "O" : 0,
        "~" : 1
    }
    right = {
        "O" : 1,
        "~" : 0
    }
    dir = right
    count = 0
    
    while i < len(town):
        if town[i] == "P":
            dir = left
            i += 1
        elif town[i] in "O~":
            count += dir[town[i]]
            i += 2
        else:
            i += 1 
    return count