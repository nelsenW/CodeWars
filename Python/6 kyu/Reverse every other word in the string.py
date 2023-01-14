import re
def reverse_alternate(s):
    result = []
    for idx, word in enumerate(re.sub(r'\s+', " ", s).split()):
        if(idx % 2 != 0):
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result).strip()