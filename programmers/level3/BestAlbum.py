from heapq import heappush, heappop

def solution(genres, plays):
    hash = {}
    for i in range(len(genres)):
        if genres[i] not in hash:
            hash[genres[i]] = []
            
        heappush(hash[genres[i]], (-1 * plays[i], i))

    tmp = []
    for _, v in hash.items():
        tmp.append(v)
    
    tmp.sort(key = lambda t: sum(-1 * v[0] for v in t), reverse=True)

    album = []
    for v in tmp:
        if len(v) == 1:
            album.append(heappop(v)[1])
            continue

        first = heappop(v)
        second = heappop(v)

        if -first[0] > -second[0]:
            album.append(first[1])
            album.append(second[1])
            continue
            
        if first[1] < second[1]:
            album.append(first[1])
            album.append(second[1])
        else:
            album.append(second[1])
            album.append(first[1])

    return album


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
ans = solution(genres, plays)
print(ans)