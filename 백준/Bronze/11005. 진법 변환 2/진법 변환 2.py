import sys

N, B = map(int,sys.stdin.readline().rstrip().split())

answer = ""

while N > 0:
    a = N % B
    if a > 9:
        answer += chr(a+55)
    else:
        answer += str(a)
    N = N // B
answer = answer[::-1]
print(answer)