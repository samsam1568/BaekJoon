import sys

N = int(sys.stdin.readline())
arr = [list(map(str,input().split())) for _ in range(N)]
mydic = dict()

for a in arr:
    ext = a[0].split('.')
    if ext[1] in mydic.keys():
        mydic[ext[1]] += 1
    else:
        mydic[ext[1]] = 1
mydic = sorted(mydic.items(), key=lambda x: x[0])
for i, j in mydic:
    print(i, j)