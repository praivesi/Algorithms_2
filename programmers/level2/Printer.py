def solution(priorities, location):
    answer = 0
    cnts = [0 for _ in range(10)]

    for pr in priorities:
        cnts[pr] += 1

    target_p = priorities[location]
    priorities[location] = -1

    for highest_pr in range(9, target_p, -1):
        if cnts[highest_pr] == 0: continue

        while priorities:
            p = priorities[0]
            priorities.pop(0)

            if p < highest_pr:
                priorities.append(p)
                continue

            cnts[highest_pr] -= 1
            answer += 1
            if cnts[highest_pr] == 0: break

    for pr in priorities:
        if pr == target_p:
            answer += 1
        
        if pr == -1:
            answer += 1
            break

    return answer

priorities = [2, 1, 3, 2]
location = 2
ans = solution(priorities, location)
print('ans => ' + f'{ans}')