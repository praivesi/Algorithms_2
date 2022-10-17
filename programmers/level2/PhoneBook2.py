def partition(array, count):
    bucket = [[] for _ in range(10)]

    for i in range(len(array)):
        if len(array[i]) <= count:
            return False
        bucket[int(array[i][count])].append(array[i])

    for bi in range(len(bucket)):
        if len(bucket[bi]) > 1 and not partition(bucket[bi], count + 1):
            return False

    return True

def solution(phone_book):
    return partition(phone_book, 0)



phone_book = ["12","123","1235","567","88"]
ans = solution(phone_book)
print('ans => ' + f'{ans}')