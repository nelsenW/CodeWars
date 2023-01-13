def contain_all_rots(strng, arr):
    i = 0
    while i < len(strng):
        if((strng[i:] + strng[0:i]) not in arr):
            return False
        i+=1
    return True