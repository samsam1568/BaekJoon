import sys

S = sys.stdin.readline().strip()
word = ""
word_list = []
for i in range(1,len(S)+1):
    word = S[-i] + word
    word_list.append(word)
word_list.sort()

for i in word_list:
    print(i)