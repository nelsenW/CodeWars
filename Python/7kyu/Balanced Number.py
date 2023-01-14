import math
def balanced_num(number):
    left_sum = 0
    right_sum = 0 
    for idx, dig in enumerate(str(number)):
        if idx < math.floor(len(str(number)) / 2):
            if(len(str(number)) % 2 == 0 and idx == (len(str(number)) / 2) -1):
                continue
            else:
                left_sum += int(dig)
        elif idx > math.floor(len(str(number)) / 2):
            right_sum += int(dig)
    
    return "Balanced" if left_sum == right_sum else "Not Balanced"