def solution(s):
    answer = []

    iterCount = 0
    zeroCount = 0
    while s != '1':
        iterCount += 1
        count = 0

        for sp in list(s):
            if sp == '1':
                count += 1
            else:
                zeroCount += 1

        s = f'{bin(count).replace("0b", "")}'


    answer.append(iterCount)
    answer.append(zeroCount)
    return answer

ans = solution('1111111')
print('ans: ' + f'{ans}')