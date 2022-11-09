def solution(a, b):
    if a > b:
        swap = a
        a = b
        b = swap    


    return sum(x for x in range(a, b + 1))
