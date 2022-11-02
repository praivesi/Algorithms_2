def solution(dirs):
    visited = []
    for i in range(6):
        visited.append([])
        for j in range(6):
            visited[i].append([])
            for k in range(6):
                visited[i][j].append([])
                for _ in range(6):
                    visited[i][j][k].append(False)
    
    routeCnt = 0
    pos = [0, 0]

    i = 0
    for d in list(dirs):
        print("f'{i}' th step >>> " + f'{d}' + ', x: ' + f'{pos[0]}' + ', y: ' + f'{pos[1]}')

        print('visited[0][0][1][0] => ' + f'{visited[0][0][1][0]}')
        print('visited[1][0][2][0] => ' + f'{visited[0][0][1][0]}')
        print('visited[2][0][3][0] => ' + f'{visited[0][0][1][0]}')
        print('visited[3][0][4][0] => ' + f'{visited[0][0][1][0]}')
        print('visited[4][0][5][0] => ' + f'{visited[0][0][1][0]}')

        if d == 'L':
            if pos[0] == -5: continue
            if not visited[pos[0]][pos[1]][pos[0] - 1][pos[1]]:
                visited[pos[0]][pos[1]][pos[0] - 1][pos[1]] = True
                visited[pos[0] - 1][pos[1]][pos[0]][pos[1]] = True
                print(f'{i}' + 'th L visited.')
                routeCnt += 1
            pos[0] -= 1

        elif d == 'R':
            if pos[0] == 5: continue
            print('TF => ' + f'{pos[0]}' + ', ' + f'{pos[1]}' + ', ' + f'{pos[0] + 1}' + ', ' + f'{pos[1]}')
            print('TF => ' + f'{visited[pos[0]][pos[1]][pos[0] + 1][pos[1]]}')
            print('visited[pos[0]] => ' + f'{visited[pos[0]]}')
            print('visited[pos[0]][pos[1]] => ' + f'{visited[pos[0]][pos[1]]}')
            print('visited[pos[0]][pos[1]][pos[0] + 1] => ' + f'{visited[pos[0]][pos[1]][pos[0] + 1]}')
            print('visited[pos[0]][pos[1]][pos[0] + 1][pos[1]] => ' + f'{visited[pos[0]][pos[1]][pos[0] + 1][pos[1]]}')
            if not visited[pos[0]][pos[1]][pos[0] + 1][pos[1]]:
                print("True invoked >>> " + ', x: ' + f'{pos[0]}' + ', y: ' + f'{pos[1]}' + ', next x: ' + f'{pos[0] + 1}' + ', next y: ' + f'{pos[1]}') 
                # visited[pos[0]][pos[1]][pos[0] + 1][pos[1]] = True
                visited[pos[0]][pos[1]][pos[0] + 1][pos[1]] = True
                visited[pos[0] + 1][pos[1]][pos[0]][pos[1]] = True
                print(f'{i}' + 'th R visited.')
                
                routeCnt += 1
            pos[0] += 1

        elif d == 'U':
            if pos[1] == 5: continue
            if not visited[pos[0]][pos[1]][pos[0]][pos[1] + 1]:
                visited[pos[0]][pos[1]][pos[0]][pos[1] + 1] = True
                visited[pos[0]][pos[1] + 1][pos[0]][pos[1]] = True
                print(f'{i}' + 'th U visited.')
                routeCnt += 1
            pos[1] += 1

        else: # 'D'
            if pos[1] == -5: continue
            if not visited[pos[0]][pos[1]][pos[0]][pos[1] - 1]:
                visited[pos[0]][pos[1]][pos[0]][pos[1] - 1] = True
                visited[pos[0]][pos[1] - 1][pos[0]][pos[1]] = True
                print(f'{i}' + 'th D visited.')
                routeCnt += 1
            pos[1] -= 1
        
        i += 1

    return routeCnt

dirs = "LLLLLLLLLLRRRRRRRRRR"
ans = solution(dirs)
print(ans)