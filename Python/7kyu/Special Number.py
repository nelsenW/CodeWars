def special_number(number):
    for char in str(number):
        if char not in "012345":
            return "NOT!!"
    return "Special!!"