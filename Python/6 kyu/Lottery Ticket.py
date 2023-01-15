def bingo(ticket,win):
    count = 0
    for mini in ticket:
        for char in mini[0]:
            if char == chr(mini[1]):
                count += 1
    return "Winner!" if count >= win else "Loser!"