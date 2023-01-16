import re
def abbreviate(s):
    return re.sub(r'([a-zA-Z])([a-zA-Z]{2,})([a-zA-Z])', lambda x: x.group(1) + str(len(x.group(2))) + x.group(3), s)