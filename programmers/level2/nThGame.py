def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = []
    words = []
    wl = 0
    for i in range(t * m):
        s = convert(i, n)
        words.append(s)
        wl += len(s)

        if wl >= t * m: break

    s = ''.join(words)

    idx = p - 1
    sl = list(s)
    for i in range(t):
        answer.append(s[idx + i * m])
    
    return ''.join(answer)

n = 16
t = 16
m = 2
p = 2
ans = solution(n, t, m, p)
print('ans => ' + f'{ans}')



