import sys

N = int(sys.stdin.readline().rstrip())
N_arr = set(map(int,sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
M_arr = list(map(int,sys.stdin.readline().rstrip().split()))
answer = []
for i in M_arr:
    if i in N_arr:
        answer.append(1)
    else:
        answer.append(0)

print(* answer)