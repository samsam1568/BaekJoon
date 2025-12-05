import sys

N = sys.stdin.readline().strip()

tmp = []

for i in N:
    tmp.append(int(i))
tmp.sort(reverse=True)
if sum(tmp) % 3 != 0 or tmp[-1] != 0 :
    print(-1)
else:
    a = ""
    for i in tmp:
        a += str(i)
    print(a)