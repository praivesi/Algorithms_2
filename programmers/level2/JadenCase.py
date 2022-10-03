def solution(s):
    splits = s.split(' ')
    answer = []

    for split in splits:
        loc_splits = list(split)
        
        for i in range(len(loc_splits)):
            if i == 0:
                if loc_splits[i] >= 'a' and loc_splits[i] <= 'z':
                    loc_splits[i] = loc_splits[i].upper()
            else:
                if loc_splits[i] >= 'A' and loc_splits[i] <= 'Z':
                    loc_splits[i] = loc_splits[i].lower()
        
        answer.append(''.join(loc_splits))

    return ' '.join(answer)

print(solution('happy birThday to you'))