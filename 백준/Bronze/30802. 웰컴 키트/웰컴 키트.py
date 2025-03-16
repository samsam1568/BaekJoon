import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
T, P = map(int, sys.stdin.readline().rstrip().split())

answer = sum((i + T - 1) // T for i in arr)  # 올림 나눗셈 처리

print(answer)
print(N // P, N % P)  # 몫과 나머지 출력
