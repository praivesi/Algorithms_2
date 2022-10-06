def solution(s):
    stack = []

    for sp in list(s):
        if sp == '(':
            stack.append(sp)
        else:
            if len(stack) == 0:
                stack.append(sp)
                continue

            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(sp)

    return True if len(stack) == 0 else False


ans = solution('(()(')
print('ans: ' + f'{ans}')