def solution(A, B):
    ah = {}
    for a in A:
        if a not in ah:
            ah[a] = 0
        ah[a] += 1
        
    bh = {}
    for b in B:
        if b not in bh:
            bh[b] = 0
        bh[b] += 1

    aa = []
    bb = []
    for k, v in ah.items():
        aa.append([k, v])

    for k, v in bh.items():
        bb.append([k, v])

    aa.sort(key = lambda a: a[0])
    bb.sort(key = lambda b: b[0])

    wc = 0
    ai = 0
    bi = 0

    while ai < len(aa) and bi < len(bb):
        if aa[ai][0] < bb[bi][0]:
            if aa[ai][1] <= bb[bi][1]:
                wc += aa[ai][1]
                bb[bi][1] -= aa[ai][1]
                ai += 1
                continue
            else:
                wc += bb[bi][1]
                aa[ai][1] -= bb[bi][1]
                bi += 1
                continue
        else:
            bi += 1

    return wc       

A = [2,2,2,2]
B = [1,1,1,1]
ans = solution(A, B)
print(ans)