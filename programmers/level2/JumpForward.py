def solution(n):
    way = [0, 1, 2]

    for i in range(n + 1):
        if i <= 2:
            continue

        way.append((way[i - 1] + way[i - 2]) % 1234567)

    return way[n]


ans = solution(4)
print('ans => ' + f'{ans}')