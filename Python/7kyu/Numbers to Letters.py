def switcher(arr):
    alpha = ' ?!abcdefghijklmnopqrstuvwxyz '
    ans = []
    for num in arr:
        ans.append(alpha[::-1][int(num)])
    return ''.join(ans)
            