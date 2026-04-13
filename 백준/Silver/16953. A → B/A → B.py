import math


A,B = map(int,input().split())
cnt = 0
answer = math.inf

def solution(nNumber, tNumber, cnt):
    global answer

    if nNumber > tNumber:
        return -1
    
    if nNumber == tNumber:
        if answer > cnt:
            answer = cnt
        
        return answer
    
    solution(int(str(nNumber)+"1"),tNumber,cnt+1)
    solution(nNumber*2,tNumber,cnt+1)

    return cnt

solution(A, B, 0)  # ← 호출 추가

if answer == math.inf:
    print(-1)
else:
    print(answer+1)