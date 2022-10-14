def solution(n, computers):
    q = []
    network = 0

    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i]: continue

        for j in range(n):
            if i == j or visited[j]: continue

            if computers[i][j] == 1:
                network += 1

                q.append(i)
                q.append(j)

                while q:
                    top = q[0]
                    q.pop(0)

                    if visited[top]: continue
                    visited[top] = True

                    for k in range(n):
                        if top == k or visited[k]: continue

                        if computers[top][k]:
                            q.append(k)

    for v in visited:
        if v: continue

        network += 1

    return network 

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
ans = solution(n, computers)
print('ans => ' + f'{ans}')