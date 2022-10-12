def solution(s):
    answer = 0

    arr = list(s)

    for i in range(len(arr)):
        stack = []

        for j in range(len(arr)):
            idx = (i + j) % len(arr)

            if arr[idx] == '(' or arr[idx] == '{' or arr[idx] == '[':
                stack.append(arr[idx])
                continue

            if arr[idx] == ')':
                if len(stack) != 0 and stack[-1] == '(': stack.pop(-1)
                else: stack.append(arr[idx])

            if arr[idx] == '}':
                if len(stack) != 0 and stack[-1] == '{': stack.pop(-1)
                else: stack.append(arr[idx])

            if arr[idx] == ']':
                if len(stack) != 0 and stack[-1] == '[': stack.pop(-1)
                else: stack.append(arr[idx])

        if len(stack) == 0:
            answer += 1        

    return answer

s = "{{{}"
ans = solution(s)
print('ans => ' + f'{ans}')