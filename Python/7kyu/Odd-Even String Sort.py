def sort_my_string(s):
    odd = ""
    even = ""
    for idx, char in enumerate(s):
        if idx % 2 == 0:
            even += char
        else:
            odd += char
    return f'{even} {odd}'