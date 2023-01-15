def min_sum(arr):
    sum = 0
    arr.sort()
    while arr:
        sum += (arr[0] * arr[-1])
        arr = arr[1:-1]
    return sum
    