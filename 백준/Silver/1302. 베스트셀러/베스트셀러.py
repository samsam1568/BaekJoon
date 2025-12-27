N = int(input())

mydic = dict()

for i in range(N):
    word = input()
    if word in mydic:
        mydic[word] += 1
    else:
        mydic[word] = 1

mydic = sorted(mydic.items(), key=lambda x: (-x[1], x[0]))

print(mydic[0][0])
