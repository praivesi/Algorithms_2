def solution(n, left, right):
    answer = []
    
    left_row = left // n

    row = left_row
    pos = left % n
    for i in range(right - left + 1):
        v = (row + 1) if pos <= row else pos + 1
        answer.append(v)

        if pos == n - 1:
            row += 1
            pos = 0
        else:
            pos += 1

    return answer

n = 4
left = 7
right = 14
ans = solution(n, left, right)
print('ans => ' + f'{ans}')