import math

def solution(arr):
    answer = arr[0]

    for a in arr:
        answer = int((a * answer) / math.gcd(a, answer))
    
    return answer


arr = [2,6,8,14]
ans = solution(arr)

print('ans => ' + f'{ans}')

