import sys

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


n = int(sys.stdin.readline())
i = 0
while i < n:
    mList = list(map(int, sys.stdin.readline().split()))
    target = mList[0]
    mList = mList[1:]
    answer = 0
    for j in range(len(mList)):
        for k in range(j+1,len(mList)):
            if j == k:
                continue
            answer += gcd(mList[j], mList[k])

    print(answer)
    i += 1