import math

def solution(progresses, speeds):
    answer = []

    while progresses:
        needDays = math.ceil((100 - progresses[0]) / speeds[0])

        popEnd = 0
        for i, p in enumerate(progresses):
            if i == 0: continue
            
            if p + speeds[i] * needDays >= 100:
                popEnd = i
            else:
                break

        answer.append(popEnd + 1)
        
        if popEnd < len(progresses) - 1:
            progresses = progresses[(popEnd + 1):]
            speeds = speeds[(popEnd + 1):]
        else: break
    
    
    return answer

    
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
ans = solution(progresses, speeds)
print('ans => ' + f'{ans}')