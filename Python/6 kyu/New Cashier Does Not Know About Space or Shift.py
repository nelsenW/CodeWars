import re
def get_order(order):
    ticket = re.findall(("burger|fries|chicken|pizza|sandwich|onionrings|milkshake|coke"), order)
    sort_order  = ["burger","fries","chicken","pizza","sandwich","onionrings","milkshake","coke"]
    ticket.sort(key = lambda x: sort_order.index(x))
    return " ".join(ticket).title()
    