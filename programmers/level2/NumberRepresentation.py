def solution(n):
    answer = 0

    for i in range(1, n + 1):
        maxCount = int(n / i)

        find = False

        num = i
        sum = 0
        iterCount = 1
        while num <= n:
            if iterCount > maxCount:
                break

            sum += num

            if sum == n:
                find = True
                break

            num += 1
            iterCount += 1

        if find:
            answer += 1
    
    return answer


ans = solution(15)

print('ans => ' + f'{ans}')