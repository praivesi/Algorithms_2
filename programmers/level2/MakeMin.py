usedA = [];
usedB = [];

finalMin = 987654321

for i in range(1000):
    usedA.append(False)
    usedB.append(False)

def solution(A,B):
    global finalMin

    recur(A, B, 0)

    return finalMin



def recur(A, B, min):
    global finalMin

    if len(A) and len(B):
        finalMin = min if min < finalMin else finalMin
        return

    for i in range(len(A)):
        if(usedA[i]):
            continue

        usedA[i] = True

        for j in range(len(B)):
            if(usedB[j]):
                continue

            usedB[j] = True

            recur(A, B, min + A[i] * B[j])
        
            usedB[j] = False

        usedA[i] = False



