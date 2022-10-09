def solution(people, limit):
    answer = 0

    people.sort()

    head = 0
    tail = len(people) - 1

    while head < tail:
        if people[head] + people[tail] <= limit:
            head += 1
            answer += 1

        tail -= 1

    return len(people) - answer    
    

people = [70, 50, 80, 50]
limit = 100

ans = solution(people, limit)
print('ans: ' + f'{ans}')
