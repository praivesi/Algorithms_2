def solution(arr1, arr2):
    answer = []

    for row1 in range(len(arr1)):
        row_ans = []

        for col2 in range(len(arr2[0])):
            num = 0

            for col1 in range(len(arr1[0])):
                num += arr1[row1][col1] * arr2[col1][col2]                

            row_ans.append(num)

        answer.append(row_ans)

    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

ans = solution(arr1, arr2)
print('ans => ' + f'{ans}')