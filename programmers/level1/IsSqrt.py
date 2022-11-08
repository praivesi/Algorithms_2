import math

def solution(n):
    ans = math.sqrt(n) 
    if ans * 10 % 10 == 0: return (ans + 1) * (ans + 1)

    return -1