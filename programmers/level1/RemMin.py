def solution(arr):
    min = 987654321
    minIdx = -1

    for i, a in enumerate(arr):
        if a < min:
            min = a
            minIdx = i

    del arr[minIdx]

    return arr if len(arr) > 0 else [-1]


arr = [4, 3, 2, 1]
ans = solution(arr)
print(ans)