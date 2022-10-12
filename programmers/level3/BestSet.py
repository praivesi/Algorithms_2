def solution(n, s):
    base = s // n
    rem = s % n

    answer = []

    if base == 0:
        return [-1]

    for i in range(n - rem):
        answer.append(base)

    for _ in range(rem):
        answer.append(base + 1)

    answer.sort()

    return answer


n = 2
s = 8
ans = solution(n, s)
print('ans => ' + f'{ans}')