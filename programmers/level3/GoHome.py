M = 0
N = 0
DP = []

def recur(m, n):
    global DP, M, N

    if m == M - 1 and n == N: return 1
    if m == M and n == N - 1: return 1
    if m == M - 1 and n == N - 1: return 2
    if m == M and n == N: return 0
    if m > M or n > N: return 0
    if DP[m][n] == -2: return 0
    if DP[m][n] > -1: return DP[m][n]

    cnt = 0
    cnt = (recur(m + 1, n) + cnt) % 1000000007
    cnt = (recur(m, n + 1) + cnt) % 1000000007

    DP[m][n] = cnt

    return cnt % 1000000007



def solution(m, n, puddles):
    global DP, M, N
    M = m
    N = n

    DP = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for pud in puddles:
        DP[pud[0]][pud[1]] = -2

    answer = recur(1, 1)

    return answer

m = 4
n = 3
puddles = [[2, 2]]
ans = solution(m, n, puddles)
print(ans)