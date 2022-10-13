def solution(s):
    answer = []

    splits = s.split('},{')
    sorted_splits = sorted(splits, key=len)

    used = []

    for i in range(100001):
        used.append(False)

    num = 0
    for j in range(len(sorted_splits)):
        ss = list(sorted_splits[j])
        print('ss => ' + f'{ss}')

        num = 0
        for i in range(len(ss)):
            if ss[i] == '{' or ss[i] == '}':
                continue
            elif ss[i] != ',':
                num *= 10
                num += int(ss[i])
            else:
                if used[num]:
                    num = 0
                    continue
                
                answer.append(num)
                used[num] = True

                num = 0

        if num != 0 and used[num] == False:
            answer.append(num)
            used[num] = True
        
    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
ans = solution(s)
print('ans => ' + f'{ans}')