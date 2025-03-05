import sys
N = int(input())
for test_case in range(N):
    word = sys.stdin.readline().strip()
    print(word[0],end="")
    print(word[-1])
