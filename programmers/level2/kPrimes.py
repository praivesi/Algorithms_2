import math

def isP(n):
    if n == 1: return False

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0: return False
    
    return True

def solution(n, k):
    rem = n
    kn = []
    while rem >= k:
        kn.insert(0, rem % k)
        rem //= k

    kn.insert(0, rem)

    kns = ""
    for kni in kn:
        kns += f'{kni}'

    knss = list(filter(None, kns.split('0')))
    cands = [int(e) for e in knss]

    answer = 0
    for c in cands:
        if isP(c): answer += 1
    
    return answer


n = 6478939023840
k = 10
ans = solution(n, k)
print('ans => ' + f'{ans}')