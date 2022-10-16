def solution(phone_book):
    first_hash = [[] for _ in range(10)]
    first_hash[0] = phone_book

    q = []
    q.append(first_hash)

    # q = [phone_book]
    # print('q => ' + f'{q}')

    while q:
        hash = q.pop(0)
        # print('hash => ' + f'{hash}')

        for h in hash:
            if len(h) > 1 and any(v == '' for v in h):
                return False
            
            if len(h) != 0:
                next_hash = [[] for _ in range(10)]
                for v in h:
                    # print('v => ' + f'{v}')
                    if len(v) == 0: continue
                    # if v == '': 
                        # print('v is empty')
                        # continue
                    next_hash[int(v[0])].append(v[1:])

                    # print('v => ' + f'{v}')
                    # print('v[0] => ' + f'{v[0]}')
                    # if len(v) >= 2:
                        # print('v[1] => ' + f'{v[1]}')
                    # print('v[1:] => ' + f'{v[1:]}')
                    # print('next_hash => ' + f'{next_hash}')
                
                q.append(next_hash)

    return True


phone_book = ["123","456","789"]
# phone_book = ["123", "456", "4568"]
ans = solution(phone_book)
print('ans => ' + f'{ans}')