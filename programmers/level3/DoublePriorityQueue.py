def solution(operations):
    q = []

    sorted = False
    for op in operations:
        ss = op.split(' ')
        if ss[0] == 'I':
            q.append(int(ss[1]))
            sorted = False
        else:
            if not q: continue

            if sorted == False:
                q.sort()
                sorted = True

            if ss[1] == '1':
                q.pop(-1)
            else:
                q.pop(0)

    if not q:
        return [0, 0]
    else:
        q.sort()
        return [q[-1], q[0]]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
ans = solution(operations)
print('ans => ' + f'{ans}')