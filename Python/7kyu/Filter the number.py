import re

def filter_string(string):
    return int("".join(re.findall("[0-9]", string)))