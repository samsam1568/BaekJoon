import sys

N = int(sys.stdin.readline().rstrip())
word = []

for _ in range(N):
    word.append(sys.stdin.readline().rstrip())

word = set(word)
word = list(word)
word.sort()
word.sort(key=len)
for k in word:
    print(k)