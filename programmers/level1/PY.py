def solution(s):
    p = 0
    y = 0

    for c in list(s):
        if c == 'p' or c == 'P': p += 1
        elif c == 'y' or c == 'Y': y += 1
    
    if p == 0 and y == 0: return True

    return p == y
    