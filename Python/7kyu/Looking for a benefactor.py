import math
def new_avg(arr, newavg):
    navg = math.ceil(newavg * (len(arr) + 1) - sum(arr))
    if navg > 0:
        return navg
    else:
        raise ValueError("Error expected")
