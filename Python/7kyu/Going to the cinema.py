import math
def movie(card, ticket, perc):
    count = 0
    tt = 0
    ct = card
    discounted = ticket
    while tt <= math.ceil(ct):
        count += 1
        tt += ticket
        discounted *= perc
        ct += discounted
    return count