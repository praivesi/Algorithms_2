import math

def get_min(date):
    s = date.split(':')
    return int(s[0]) * 60 + int(s[1])

def solution(fees, records):
    answer = []

    splits = [rec.split(' ') for rec in records]
    recs = sorted(splits, key= lambda x: (x[1], x[0]))

    if len(recs) == 1: 
        stay = 1439 - get_min(recs[0][0])
        fee = fees[1] + math.ceil((stay - fees[0]) / fees[2]) * fees[3] if stay > fees[0] else fees[1]
        answer.append(int(fee))
        return answer

    stay = 0
    for i, rec in enumerate(recs):
        if i == 0: continue

        if rec[1] == recs[i - 1][1]:
            if rec[2] == 'OUT':
                stay += get_min(rec[0]) - get_min(recs[i - 1][0])
        else:
            if recs[i - 1][2] == 'IN':
                stay += 1439 - get_min(recs[i - 1][0])

            fee = fees[1] + math.ceil((stay - fees[0]) / fees[2]) * fees[3] if stay > fees[0] else fees[1]
            answer.append(int(fee))
            stay = 0

        if i == len(recs) - 1:
            if rec[2] == 'IN':
                stay += 1439 - get_min(recs[i][0])

            fee = fees[1] + math.ceil((stay - fees[0]) / fees[2]) * fees[3] if stay > fees[0] else fees[1] 
            answer.append(int(fee))
            break

    return answer

fees =[180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# records =  ["05:34 5961 IN", "06:34 5961 OUT", "07:34 5961 IN", "08:34 5961 OUT", "09:34 5961 IN", "10:34 5961 OUT", "11:34 5961 IN", "12:34 5961 OUT"]
ans = solution(fees, records)
print('ans => ' + f'{ans}')