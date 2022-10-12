def solution(citations):
    citations.sort(reverse=True)

    for h in range(citations[0], -1, -1):
        for i, cit in enumerate(citations):
            if cit >= h:
                continue

            if i >= h:
                return h
            else:
                break

    return citations[0] if len(citations) >= citations[0] else len(citations)

citations = [3, 0, 6, 1, 5]
ans = solution(citations)
print('ans => ' + f'{ans}')