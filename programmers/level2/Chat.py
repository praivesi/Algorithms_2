def solution(record):
    answer = []

    nic_d = {}
    change_d = {}
    log = []

    for r in record:
        split = r.split(' ')

        if split[0] == 'Enter':
            log.append(['들어왔습니다.', split[1]])
        elif split[0] == 'Leave':
            log.append(['나갔습니다.', split[1]])
            continue
        else: # Change
            change_d[split[1]] = split[2]
            
        nic_d[split[1]] = split[2]

    for cd in change_d:
        nic_d[cd[0]] = cd[1]

    for l in log:
        msg = nic_d[l[1]] + '님이 ' + l[0]
        answer.append(msg)

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
ans = solution(record)
print(ans)