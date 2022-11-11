visited = []
numbers = []

def get_cnt(sum, curman, usedman):

    global visited, numbers
    
    if usedman == 3:
        if sum == 0: return 1
        else: return 0
    
    cnt = get_cnt(sum, curman + 1, usedman)

    visited[curman] = True
    cnt += get_cnt(sum + numbers[curman], curman + 1, usedman + 1)
    visited[curman] = False


def solution(number):
    global visited, numbers
    
    visited = [False for _ in range(len(number))]
    numbers = []

    return get_cnt(0, 0, 0)    