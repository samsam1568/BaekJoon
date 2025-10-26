import sys

N = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
coordinate = []

for a,b in arr:
    coordinate.append([a,a+10,b,b+10]) #left #right #bottom #top

rect = []

for k in coordinate:
    for i in range(k[0],k[1]):
        for j in range(k[2], k[3]):
            if [i,j] in rect:
                continue
            rect.append([i,j])
print(len(rect))