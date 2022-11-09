def solution(x):
    agg = 0
    tmp = x

    while tmp:
        agg += tmp % 10
        tmp //= 10
    
    return (x / agg) * 10 % 10 == 0
