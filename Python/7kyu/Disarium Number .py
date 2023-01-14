def disarium_number(number):
    dis = 0 
    for idx, dig in enumerate(str(number)):
        dis += (int(dig) ** (idx + 1))
    return "Disarium !!" if number == dis else "Not !!"