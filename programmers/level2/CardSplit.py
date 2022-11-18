def solution(arrayA, arrayB):
    adiv = []
    anotdiv = []
    bdiv = []
    bnotdiv = []

    
    for cand in range(1, max(arrayA) + 1):
        dividable = False
        for a in arrayA:
            if a % cand == 0:
                dividable = True
                break
        
        if not dividable:
            anotdiv.append(cand)
        
        dividable = True
        for a in arrayA:
            if a % cand != 0:
                dividable = False
                break
        
        if dividable:
            adiv.append(cand)

    for cand in range(1, max(arrayB) + 1):
        dividable = False
        for b in arrayB:
            if b % cand == 0:
                dividable = True
                break
        
        if not dividable:
            bnotdiv.append(cand)
        
        dividable = True
        for b in arrayB:
            if b % cand != 0:
                dividable = False
                break
        
        if dividable:
            bdiv.append(cand)
    
    adiv.sort(reverse= True)
    anotdiv.sort(reverse= True)
    bdiv.sort(reverse= True)
    bnotdiv.sort(reverse= True)

    firstcase = 0
    secondcase = 0
    
    for ad in adiv:
        if ad in bnotdiv:
            firstcase = ad
            break
    
    for bd in bdiv:
        if bd in anotdiv:
            secondcase = bd
            break
    
    return max(firstcase, secondcase)

arrayA = [10, 20]
arrayB = [5, 17]
ans = solution(arrayA, arrayB)
print(ans)