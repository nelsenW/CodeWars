def find_nb(m):
    sum = 0
    i = 1
    while sum < m:
        sum += i ** 3
        i += 1
    return i - 1 if sum == m else -1