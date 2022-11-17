def solution(want, number, discount):
    answer = 0
    wp = {}
    dp = {}
    
    for i in range(len(want)):
        wp[want[i]] = number[i]
    
    if len(discount) < 10:
        for d in discount:
            if d not in dp: dp[d] = 0
                
            dp[d] += 1
            
        valid = True
        for wk, wv in wp.items():
            if wk not in dp: 
                valid = False
                break

            if dp[wk] < wv:
                valid = False
                break
        
        if valid: answer += 1
             
    else:
        for i in range(len(discount)):
            if i == len(discount) - 9: break 

            if i == 0:
                for j in range(10):
                    if discount[j] not in dp: dp[discount[j]] = 0
                
                    dp[discount[j]] += 1
            else:
                dp[discount[i - 1]] -= 1
                
                if discount[i + 9] not in dp: dp[discount[i + 9]] = 0
                
                dp[discount[i + 9]] += 1
                
            valid = True
            
            for wk, wv in wp.items():
                if wk not in dp: 
                    valid = False
                    break

                if dp[wk] < wv:
                    valid = False
                    break
            
            if valid: answer += 1   

    return answer

want = ["apple"]
number = [10]
discount =	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

ans = solution(want, number, discount)
print(ans)
    