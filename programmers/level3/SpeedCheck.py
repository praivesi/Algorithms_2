def solution(routes):
    answer = 0

    routes.sort(key = lambda r: r[1])

    end = -30001
    for r in routes:
        if r[0] > end:
            answer += 1
            end = r[1]
            continue

    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
ans = solution(routes)
print(ans)