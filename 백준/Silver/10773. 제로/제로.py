import sys

K = int(sys.stdin.readline().rstrip())
now_num = []
for i in range(K):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        now_num.pop()
    else:
        now_num.append(num)
if len(now_num) == 0:
    print(0)
else:
    print(sum(now_num))
