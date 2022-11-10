def solution(n):
    for i in range(1, n):
        q = int(n / i)
        if n - q * i == 1: return i
        
    return n - 1