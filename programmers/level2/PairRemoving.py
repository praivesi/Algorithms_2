def solution(s):
    stack = []

    chars = list(s)

    for i in range(len(chars)):
        if len(stack) == 0:
            stack.append(chars[i])
            continue
            
        if stack[-1] == chars[i]:
            stack.pop()
            continue
    
        stack.append(chars[i])
    

    return 1 if len(stack) == 0 else 0
        



s = "baabaa"
ans = solution(s)
print('ans = ' + f'{ans}')