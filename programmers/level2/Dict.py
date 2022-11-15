answer = 0
idx = -1

def solution(word):
    global answer, idx

    alphabets = ['A', 'E', 'I', 'O', 'U']

    def dfs(str):
        global answer, idx

        if len(str) > 5: return False

        idx += 1 

        if str == word: 
            answer = idx
            return True

        for ap in alphabets:
            if dfs(str + ap): return True
        
        return False
    
    dfs('')
        

    return answer

word = "AAAE"
ans = solution(word)
print(ans)