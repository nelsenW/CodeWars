def name_value(my_list):
    ans = []
    for idx, word in enumerate(my_list):
        count = 0
        for char in word:
            if char == " ":
                pass
            else:
                count += ord(char) - 96
        ans.append((idx+1) * count)
    return ans