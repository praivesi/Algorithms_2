def solution(numbers, target):
    answer = 0

    q = []
    q.append([0, 0])

    while q:
        state = q.pop(0)
        depth = state[0]
        agg = state[1]

        if depth == len(numbers):
            if agg == target:
                answer += 1
            continue

        q.append([depth + 1, agg + numbers[depth]])
        q.append([depth + 1, agg - numbers[depth]])

    return answer

numbers = [4, 1, 2, 1]
target = 4
ans = solution(numbers, target)
print('ans => ' + f'{ans}')