import re
def sum_of_integers_in_string(s):
    return sum(map(lambda x: int(x), re.findall("[0-9]+", s)))
 
