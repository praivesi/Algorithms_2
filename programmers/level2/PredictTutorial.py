import math

def solution(n,a,b):
    turn = 0
    while a != b:
        turn += 1

        a = math.ceil(a / 2)
        b = math.ceil(b / 2)

    return turn

ans = solution(8, 4, 7)
print('ans => ' + f'{ans}')
