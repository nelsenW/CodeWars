def race(v1, v2, g):
    if v1 >= v2:
        return None 
    hours = 1/((v2-v1)/g)
    mins = (hours - int(hours)) * 60
    seconds = (mins - int(mins)) * 60
    return [int(hours), int(mins), int(seconds)]