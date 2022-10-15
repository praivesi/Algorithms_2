import math

def solution(str1, str2):
    if str1 == "" and str2 == "": return 65536

    str1 = str1.lower()
    str2 = str2.lower()

    ss1 = [[0 for _ in range(26)] for _ in range(26)]
    ss2 = [[0 for _ in range(26)] for _ in range(26)]

    for i in range(len(str1) - 1):
        c1 = str1[i]
        c2 = str1[i + 1]
        if c1 >= 'a' and c1 <= 'z' and c2 >= 'a' and c2 <= 'z':
            ss1[ord(c1) - ord('a')][ord(c2) - ord('a')] += 1

    for i in range(len(str2) - 1):
        c1 = str2[i]
        c2 = str2[i + 1]
        if c1 >= 'a' and c1 <= 'z' and c2 >= 'a' and c2 <= 'z':
            ss2[ord(c1) - ord('a')][ord(c2) - ord('a')] += 1

    join = 0
    union = 0
    for i in range(26):
        for j in range(26):
            join += min(ss1[i][j], ss2[i][j])
            union += max(ss1[i][j], ss2[i][j])

    if union == 0: return 65536
    
    jaccard = join / union

    return math.floor(jaccard * 65536)

str1 = "E=M*C^2"
str2 = "e=m*c^2"
ans = solution(str1, str2)
print('ans => ' + f'{ans}')