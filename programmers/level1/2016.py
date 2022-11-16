def solution(a, b):
    past = 1
    
    if a != 1:
        if a < 3: past += 31
        if a < 4: past += 29
        if a < 5: past += 31
        if a < 6: past += 30
        if a < 7: past += 31
        if a < 8: past += 30
        if a < 9: past += 31
        if a < 10: past += 31
        if a < 11: past += 30
        if a < 12: past += 31
        if a < 13: past += 30
    
    past += b

    cal = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    return cal[(4 + past) % 7]