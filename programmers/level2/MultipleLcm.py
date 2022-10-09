def solution(arr):
    answer = 1
    elems = {}

    for a in arr:
        dCount = 0
        agg = 1

        if a == 2:
            elems[2] = 1        

        d = 2
        while d <= a:
            dCount += 1

            if ((a / ( d * agg)) * 10) % 10 != 0:
                dCount = 0
                d += 1
                continue

            if d in elems:
                elems[d] = max(elems[d], dCount)
            else:
                elems[d] = dCount

            agg *= d

    for e in elems:
        for i in range(elems[e]):
            answer *= e

    return answer


arr = [2,6,8,14]
ans = solution(arr)

print('ans => ' + f'{ans}')