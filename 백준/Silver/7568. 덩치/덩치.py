import sys

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int,sys.stdin.readline().rstrip().split()))for _ in range(N)]
answer = []

for w,t in arr:
    cnt = 1
    for i,j in arr:
        if w == i and t == j:
            continue
        if w < i and t < j:
            cnt += 1
    answer.append(cnt)

print(* answer)

