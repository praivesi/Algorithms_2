def recur(k, dungeons, visited):
    maxVisit = 0

    for i in range(len(visited)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True

            visitCnt =  recur(k - dungeons[i][1], dungeons, visited) + 1

            if visitCnt > maxVisit:
                maxVisit = visitCnt

            visited[i] = False

    return maxVisit

def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]

    return recur(k, dungeons, visited)

k = 80
dungeons = [[80,20],[50,40],[30,10]]
ans = solution(k, dungeons)
print(ans)