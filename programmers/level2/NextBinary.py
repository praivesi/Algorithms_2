def solution(n):
    binDigits = list(bin(n).replace('0b', ''))

    # print('binDigits: ' + f'{binDigits}')

    oneCount = 0
    for i in range(len(binDigits)):
        if binDigits[i] == '1':
            oneCount += 1
    
    # print('oneCount : ' + f'{oneCount}')

    next = n
    nextOneCount = -1

    while oneCount != nextOneCount:
        next += 1
        nextBinDigits = list(bin(next).replace('0b', ''))

        # print('nextBinDigits: ' + f'{nextBinDigits}')

        nextOneCount = 0
        for i in range(len(nextBinDigits)):
            if nextBinDigits[i] == '1':
                nextOneCount += 1

            if nextOneCount > oneCount:
                break
        
        # print('nextOneCount : ' + f'{nextOneCount}')

    return next



ans = solution(60335700574206)

print('ans: ' + f'{ans}')
