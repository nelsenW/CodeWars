def men_from_boys(arr):
    men = []
    boys = []
    for num in set(arr):
        if num % 2 == 0:
            men.append(num)
        else:
            boys.append(num)
            
    men.sort()
    boys.sort(reverse=True)
    return men + boys