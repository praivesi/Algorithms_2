def solution(n, words):
    p = [words[0][0]]
    
    for i,w in enumerate(words): # dictionart enumeration
        if w not in p and p[-1][-1] == w[0]:
            p.append(w)
        else:
            return [i % n + 1, i // n + 1]  # // => 나누기 + 소수점 이하 버리기

    return [0, 0]


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
ans = solution(n, words)
print('ans => ' + f'{ans}')