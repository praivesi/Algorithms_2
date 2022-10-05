stack = ['a', 'b', 'c']

top = stack[-1] # 맨 마지막에 있는 원소를 꺼낸다.

# stack[-1] 사용 시 주의할 점은 
# stack이 비어있는 경우 out of range 오류가 뜨기 때문에
# 아래처럼 stack의 length 체크를 해주는 게 좋다.

if len(stack) > 0: # stack의 length 체크
	print('top: ' + stack[-1])
    

# output
# top: c