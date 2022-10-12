from heapq import heappush, heappop
import math

def solution(n, works):
    heap = []

    for w in works:
        heappush(heap, w * -1)

    for i in range(n):
        longest = heap[0] * -1
        heappop(heap)

        if longest == 0: return 0

        heappush(heap, (longest - 1) * -1)

    overwork = 0
    while heap:
        overwork += pow(heap[0], 2)
        heappop(heap)

    return overwork


n = 3
works = [1, 1]
ans = solution(n, works)
print('ans => ' + f'{ans}')