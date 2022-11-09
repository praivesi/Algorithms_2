def solution(n):
    d = []

    while n:
        d.append(n % 10)
        n //= 10
    
    d.sort(reverse = True)

    answer = 0
    for dd in d:
        answer *= 10
        answer += dd
    
    return answer