import re
def hydrate(drink_string): 
    ans = sum(int(x) for x in list(re.findall("[0-9]+", drink_string))) 
    pl = "es" if ans > 1 else ""
    return f'{ans} glass{pl} of water'
