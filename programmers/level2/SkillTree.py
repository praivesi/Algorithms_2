def solution(skill, skill_trees):
    answer = 0
    order = [-1 for _ in range(26)]

    for i, sk in enumerate(list(skill)):
        order[ord(sk) - ord('A')] = i
    
    for skill_tree in skill_trees:
        used = [False for _ in range(26)]
        usable = True
        cnt = 0

        for st in list(skill_tree):
            stOrder = ord(st) - ord('A')

            if order[stOrder] == -1: continue

            if order[stOrder] > cnt:
                usable = False
                break

            if not used[stOrder]:
                used[stOrder] = True
                cnt += 1
            
        if usable: answer += 1

    return answer

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
ans = solution(skill, skill_trees)
print(ans)