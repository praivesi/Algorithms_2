def solution(s):
    answer = ''

    strings = s.split(' ')

    min = 987654321;
    max = -987654321;

    for str in strings:
        num = int(str)
        if num < min:
            min = num
        if num > max:
            max = num
        
    return f'{min}' + " " + f'{max}'