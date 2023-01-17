def divisible_by_three(st):
    st = int(st)
    while st > 9:
        st = sum(int(x) for x in list(str(st)))
    if st == 3 or st == 6 or st == 9:
        return True 
    return False