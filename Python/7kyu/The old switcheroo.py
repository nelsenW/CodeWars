import re
def vowel_2_index(string):
    s = ''
    for idx, char in enumerate(string):
        if char in "aeiouAEIOU":
            s += f'{idx + 1}'
        else:
            s += char 
    return s
        