def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    up = [[]] + [[] for _ in range(10000)] + [[]]
    

    for i, p in enumerate(prices):
        up[p].append(i)

        if up[p + 1]:
            for pi in up[p + 1]:
                answer[pi] = i - pi

    return answer

prices = [1, 2, 3, 2, 3]
ans = solution(prices)
print(ans)