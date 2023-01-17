def crap(garden, bags, cap):
    count = 0
    for row in garden:
        if 'D' in row:
            return "Dog!!"
        count += row.count("@")
    return 'Clean' if bags*cap >= count else 'Cr@p'