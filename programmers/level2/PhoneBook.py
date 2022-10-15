def solution(phone_book):
    q = [phone_book]

    while q:
        hash = q.pop(0)

        for h in hash:
            if len(h) > 1 and any(v == '' for v in h):
                return False
            elif len(h) != 0:
                next_hash = [[] for _ in range(10)]
                for v in h:
                    if len(v) == 0: continue
                    next_hash[int(v[0])].append(v[1:])
                    q.append(next_hash)

    return True


phone_book = ["119", "97674223", "1195524421"]
ans = solution(phone_book)
print('ans => ' + f'{ans}')