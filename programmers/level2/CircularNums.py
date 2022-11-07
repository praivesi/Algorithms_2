def solution(elements):
    l = []

    for i in range(1, len(elements) + 1):
        agg = 0
        for j in range(len(elements)):
            if j == 0:
                agg = sum(x for x in elements[:j + i])
                l.append(agg)
                continue
                
            agg -= elements[j - 1]
            agg += elements[(j + i - 1) % len(elements)]
            
            l.append(agg)

    s = set(l) 

    return len(s)

elements = [7, 9, 1, 1, 4]
ans = solution(elements)
print(ans)