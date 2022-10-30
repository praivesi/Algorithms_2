dp = []
LAND = []

def jump(turn, pos):
    global dp, LAND

    if turn == len(LAND): return 0
    if pos != - 1 and dp[turn][pos] != -1: return dp[turn][pos]

    maxScore = 0

    for i in range(4):
        if i == pos: continue

        curScore = jump(turn + 1, i) + LAND[turn][i]
        maxScore = curScore if curScore > maxScore else maxScore

    dp[turn][pos] = maxScore
    return maxScore


def solution(land):
    global dp, LAND

    dp = [[-1 for _ in range(4)] for _ in range(len(land))]
    LAND = land

    return jump(0, -1)

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
ans = solution(land)
print(ans)