def solution(prices):
    answer = [0 for _ in range(len(prices))]

    stack = []

    for i, p in enumerate(prices):
        if not stack:
            stack.append([i, p])
            continue
        
        if stack[-1][1] <= p: 
            stack.append([i, p])
            continue

        while stack:
            if stack[-1][1] <= p: break

            top = stack.pop(-1)
            answer[top[0]] = i - top[0]

        stack.append([i, p])
            
    while stack:
        top = stack.pop(-1)

        answer[top[0]] = len(prices) - 1 - top[0]
            
    return answer

prices =  [1, 2, 3, 2, 3]
ans = solution(prices)
print(ans)