import re
def remove_rotten(bag):
    ans = []  
    if not bag:
        return ans
    
    for fruit in bag:
        ans.append(re.sub("rotten", "", fruit).lower())
    return ans