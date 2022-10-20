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
        first = heappop(heap)

        if first >= K: 
            return answer

        if len(heap) == 0: 
            heappush(heap, first)
            break
        
        answer += 1

        second = heappop(heap)
        new_scov = first + second * 2

        heappush(heap, new_scov)
    
    first = heappop(heap)
    if first >= K:
        return answer

    return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
ans = solution(scoville, K)
print(ans)