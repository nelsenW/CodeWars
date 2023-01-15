from math import sqrt 

def is_prime(num):
    for n in range(2, int(sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

def gap(g, m, n):
    arr = []
    for num in range(m,n + 1):
        if is_prime(num):
            arr.append(num)
            if len(arr) > 1 and arr[-1] - arr[-2] == g:
                return [arr[-2], arr[-1]]
    
    return None