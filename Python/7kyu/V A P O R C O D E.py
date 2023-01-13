def vaporcode(s):
    string = []
    for char in s:
        if char == " ":
            pass
        else:
            string.append(char.upper() + "  ")
    return ''.join(string).strip()