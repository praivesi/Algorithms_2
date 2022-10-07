def solution(brown, yellow):
    answer = []

    sum = brown + yellow

    for i in range(3, int(sum / 2) + 1):
        j = sum / i

        if (j * 10) % 10 != 0:
            continue

        if (i - 2) * (j - 2) == yellow:
            answer.append(i)
            answer.append(int(j))
            break

    if answer[0] < answer[1]:
        swap = answer[0]
        answer[0] = answer[1]
        answer[1] = swap

    return answer

ans = solution(24, 24)

print('ans => ' + f'{ans}')