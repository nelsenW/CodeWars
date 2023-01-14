import re
def solve(s):
    count = [0,0,0,0]
    for char in s:
        if re.match("[A-Z]", char):
            count[0] += 1
        elif re.match("[a-z]", char):
            count[1] += 1
        elif re.match("[0-9]", char):
            count[2] += 1
        else:
            count[3] += 1
    return count