def paint_letterboxes(start, finish):
    arr = [0] * 10
    for num in range(start, finish + 1):
        for v in list(str(num)):
            arr[int(v)] += 1
    
    return arr