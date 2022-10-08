def solution(brown, yellow):
    answer = []

    sum = brown + yellow

    for i in range(3, int(sum / 2) + 1):
        j = sum / i

        if (j * 10) % 10 != 0: # 격자의 개수는 소수점이 될 수 없으므로 skip
            continue

        if (i - 2) * (j - 2) == yellow: # 위아래 각각 1줄씩 (총 2줄), 양옆 각각 1줄씩 (총 2줄) 빼면 노란 격자의 가로 세로 길이가 나옴, 그리고 (가로)*(세로)가 yellow 격자의 개수와 일치하면 그거슨 정답
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