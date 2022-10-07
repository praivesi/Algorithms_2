def solution(n):
    answer = 0
    fib = []

    fib.append(0)
    fib.append(1)

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    
    return fib[n] % 1234567


ans = solution(5)

print('ans: ' + f'{ans}')
