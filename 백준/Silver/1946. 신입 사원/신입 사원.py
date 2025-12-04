import sys

T = int(sys.stdin.readline())
mt = 0

while mt < T:
    N = int(sys.stdin.readline())
    mydict = []
    for i in range(N):
        a,b = map(int, sys.stdin.readline().split())
        mydict.append([a,b])
    mydict.sort()
    cut_line = mydict[0]
    cnt = 1

    for j in range(len(mydict)):
        if cut_line[1] > mydict[j][1]:
            cnt += 1
            if cut_line[0] < mydict[j][0]:
                cut_line = mydict[j]
    print(cnt)
    mt += 1