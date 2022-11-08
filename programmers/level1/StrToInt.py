def solution(s):
    sig = 1
    agg = 0

    for c in list(s):
        if c == '-': 
            sig = -1
            continue
        
        if c == '+': continue

        agg *= 10
        agg += int(c)

    return sig * agg

