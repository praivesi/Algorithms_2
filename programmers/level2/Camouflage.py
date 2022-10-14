def solution(clothes):
    d = {}
    for c in clothes:
        if c[1] not in d:
            d[c[1]] = []

        d[c[1]].append(c[0])
    
    answer = 1
    for _, v in d.items():
        answer *= len(v) + 1
    answer -= 1
    
    return answer        


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
ans = solution(clothes)
print('ans => ' + f'{ans}')