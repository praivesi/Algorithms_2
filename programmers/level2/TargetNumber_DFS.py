def solution(numbers, target):
    answer = 0

    def dfs(agg, depth):
        nonlocal answer

        if depth == len(numbers):
            if agg == target:
                answer += 1
            return

        dfs(agg + numbers[depth], depth + 1)
        dfs(agg - numbers[depth], depth + 1)
    
    dfs(0, 0)

    return answer


numbers = [4, 1, 2, 1]
target = 4
ans = solution(numbers, target)
print('ans => ' + f'{ans}')