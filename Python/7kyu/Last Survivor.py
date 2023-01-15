def last_survivor(letters, coords): 
    for c in coords:
        letters =  letters[:c] + letters[c+1:]
    return letters