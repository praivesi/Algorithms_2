def solution(msg):
    answer = []
    d = [{} for _ in range(26)]

    for i in range(26):
        d[i][chr(ord('A') + i)] = i + 1

    cur_idx = -1
    next_idx = 27
    s = ''
    for c in list(msg):
        s += c
        d_idx = ord(s[0]) - ord('A')

        if s in d[d_idx]:
            cur_idx = d[d_idx][s]
            continue

        answer.append(cur_idx)
        d[d_idx][s] = next_idx

        cur_idx = d[ord(c) - ord('A')][c]
        next_idx += 1
        s = c

    if cur_idx != -1:
        answer.append(cur_idx)

    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
ans = solution(msg)
print(ans)