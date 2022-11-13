def solution(n):
    str = []
    for i in range(n):
        if i % 2 == 0: str.append('수')
        else: str.append('박')
    
    return ''.join(x for x in str)