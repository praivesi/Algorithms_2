def solution(begin, target, words):
    q = []
    used = [False for _ in range(len(words))]
    q.append([begin, 0])

    while q:
        curWord = q[0][0]
        curDepth = q[0][1]
        q.pop(0)

        if curWord == target:
            return curDepth
        
        for i, w in enumerate(words):
            if used[i]: continue

            diffCnt = 0
            for j in range(len(begin)):
                if curWord[j] != w[j]:
                    diffCnt += 1

            if diffCnt == 1:
                q.append([w, curDepth + 1])
                used[i] = True

    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
ans = solution(begin, target, words)
print('ans => ' + f'{ans}')