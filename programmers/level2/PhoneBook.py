def solution(phone_book):
    first_hash = [[] for _ in range(10)]
    first_hash[0] = phone_book

    q = []
    q.append(first_hash)

    while q:
        hash = q.pop(0)

        for h in hash:
            if len(h) == 1: continue

            if len(h) > 1 and any(v == '' for v in h):
                return False
            
            if len(h) != 0:
                next_hash = [[] for _ in range(10)]
                for v in h:
                    if len(v) == 0: continue
                    next_hash[int(v[0])].append(v[1:])
                q.append(next_hash)

    return True


phone_book = ["123","456","789"]
ans = solution(phone_book)
print('ans => ' + f'{ans}')