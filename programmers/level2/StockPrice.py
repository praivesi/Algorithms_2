def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    up = [[]] + [[] for _ in range(10000)] + [[]]
    
    max_p = 0
    for i, p in enumerate(prices):
        max_p = max(p, max_p)
        up[p].append(i)

        for j in range(p + 1, max_p + 1):
            if not up[j]: continue
            
            for pi in up[j]:
                answer[pi] = i - pi
                
            up[j] = []

    for upp in up:
        if not upp: continue

        for ix, ui in enumerate(upp):
            answer[ui] = len(prices) - 1 - ui
            
    return answer


prices =  [2, 3, 1, 2, 3]
ans = solution(prices)
print(ans)