def solution(a, b):
    past = 0
    
    if a != 1:
        if a > 1: past += 31
        if a > 2: past += 29
        if a > 3: past += 31
        if a > 4: past += 30
        if a > 5: past += 31
        if a > 6: past += 30
        if a > 7: past += 31
        if a > 8: past += 31
        if a > 9: past += 30
        if a > 10: past += 31
        if a > 11: past += 30
    
    b -= 1
    past += b

    cal = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    return cal[past % 7]

ans = solution(5, 24)
print(ans)