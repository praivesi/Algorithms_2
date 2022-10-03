numStack = []
charStack = []

def solution(s):
    chars = list(s)

    num = 0

    for c in chars:
        if c >= '0' and c<= '9': # 숫자
            num *= 10
            num += int(c)
        else: # 문자
            if num != 0:
                numStack.append(num)
                num = 0
            
            if c != ')':
                charStack.append(c)
                continue
            
            curStr = []
            while len(charStack) != 0:
                curChar = charStack.pop()

                if len(curChar) > 1:
                    curStr.insert(0, curChar)
                    continue

                if curChar != '(':
                    curStr.insert(0, curChar)
                    continue
                else:
                    curNum = numStack.pop()
                    finalCurStr = ''.join(curStr)

                    decoded = []
                    for i in range(curNum):
                        decoded.append(finalCurStr)
                        
                    charStack.append(''.join(decoded))
                break
    
    rest = []
    while len(charStack) != 0:
        rest.append(charStack.pop())

    rest.reverse()
    answer = ''.join(rest)

    return answer
                
ans = solution('2(2(hi)2(co))x2(bo)')
# ans = solution('3(hi)2(co)')
print(ans)