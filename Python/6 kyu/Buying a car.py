def nbMonths(spo, spn, sp, pl):
    i = 0
    savings = 0
    while (spo + savings < spn):
        i += 1
        savings += sp
        if i % 2 == 0:
            pl += 0.5 
        spo -= spo * (pl/100)
        spn -= spn * (pl/100)
            
    return [i, -round(spn - (spo + savings))]