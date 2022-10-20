from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0

    heap = []

    for s in scoville:
        heappush(heap, s)

    min_s = heappop(heap)

    if min_s >= K: return 0

    heappush(heap, min_s)

    while heap:
        answer += 1
        first = heappop(heap)
        second = heappop(heap)
        new_scov = first + second * 2

        if new_scov >= K: break

        heappush(heap, new_scov)

        if len(heap) == 1: break
    
    if len(heap) <= 1:
        answer = -1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
ans = solution(scoville, K)
print(ans)