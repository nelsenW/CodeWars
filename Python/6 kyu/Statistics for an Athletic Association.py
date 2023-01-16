import functools

def get_range(lst):
    ans = {"h": 0, "m": 0, "s": 0}
    seconds = (lst[-1] - lst[0])
    ans["h"] = str(int(seconds / 3600)).zfill(2)
    seconds -= int(seconds/3600) * 3600
    ans["m"] = str(int(seconds / 60)).zfill(2)
    seconds -= int(seconds / 60) * 60
    ans["s"] = str(seconds).zfill(2)
    return ans

def get_avg(lst):
    ans = {"h": 0, "m": 0, "s": 0}
    seconds = functools.reduce(lambda x,y: x+y,lst) / len(lst)
    ans["h"] = str(int(seconds / 3600)).zfill(2)
    seconds -= int(seconds/3600) * 3600
    ans["m"] = str(int(seconds / 60)).zfill(2)
    seconds -= int(seconds / 60) * 60
    ans["s"] = str(int(seconds)).zfill(2)
    return ans

def get_median(lst):
    ans = {"h": 0, "m": 0, "s": 0}
    seconds = lst[int(len(lst)/2)] if len(lst) % 2 != 0 else (lst[int(len(lst)/2)] + lst[int((len(lst)/2) - 1)]) / 2
    ans["h"] = str(int(seconds / 3600)).zfill(2)
    seconds -= int(seconds/3600) * 3600
    ans["m"] = str(int(seconds / 60)).zfill(2)
    seconds -= int(seconds / 60) * 60
    ans["s"] = str(int(seconds)).zfill(2)
    return ans



def stat(strg):
    if not strg:
        return ""
    
    strg = strg.split(", ")
    strg = list(map(lambda x: x.split("|"), strg))
    strg = list(map(lambda x: (int(x[0]) * 3600) + (int(x[1]) * 60) + int(x[2]), strg))
    strg.sort()
    
    range = get_range(strg)
    average = get_avg(strg)
    median = get_median(strg)
    
    return f'Range: {"|".join(list(range.values()))} Average: {"|".join(list(average.values()))} Median: {"|".join(list(median.values()))}'