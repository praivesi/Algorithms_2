def solution(phone_number):
    sl = []

    for i, p in enumerate(list(phone_number)):
        if i < len(phone_number) - 4:
            sl.append('*')
        else:
            sl.append(p)
    
    return ''.join(sl)
