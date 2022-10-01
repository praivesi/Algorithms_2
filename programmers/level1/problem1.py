def solution(num1, num2):
    N = num1 / num2
    rest = N * 10 % 10
    goal = N * 10 - rest
    goal /= 10
    
    return goal

ans = solution(7, 2)
print(ans)