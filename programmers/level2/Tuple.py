def solution(s):
    answer = []

    s = s.replace('{', '')
    s = s.replace('}', '')
    # print('s => ' + s)

    ss = s.split(',')
    # print('ss => ' + f'{ss}')

    counts = []
    for _ in range(100001):
        counts.append(0)

    for ns in ss:
        counts[int(ns)] += 1
    
    d = {}
    for i, c in enumerate(counts):
        if c == 0: continue
        d[i] = c
    
    sd = sorted(d.items(), key = lambda item: item[1], reverse = True)
    # print('sd => ' + f'{sd}')

    for e in sd:
        answer.append(e[0])
    
    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
ans = solution(s)
print('ans => ' + f'{ans}')