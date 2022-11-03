def solution(dirs):
    answer = 0
    x = 5
    y = 5
    map = []
    move = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}

    for i in range(len(dirs)):
        (dy, dx) = move[dirs[i]]
        if not (0 <= x + dx and x + dx <= 10 and 0 <= y + dx and y + dx <= 10):
            continue
        map.append((x, y, x + dx, y + dy))
        map.append((x + dx, y + dy, x, y))
        x = x + dx
        y = y + dy
    
    mapset = set(map)
    answer = len(mapset) // 2

    return answer


dirs = "ULURRDLLU"
ans = solution(dirs)
print(ans)