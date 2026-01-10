St = input()
word = input()
Ans = 0
i = 0
while i <= len(St)-len(word):
    if word == St[i:i+len(word)]:
        Ans += 1
        i += len(word)
    else:
        i+= 1

print(Ans)