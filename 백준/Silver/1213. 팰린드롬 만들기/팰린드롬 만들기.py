import sys

sentence = sys.stdin.readline().rstrip()
mdic = dict()
answer = ""
flag = True
for i in sentence:
    if i not in mdic:
        mdic[i] = 1
    else:
        mdic[i] += 1
sorted_mdic = sorted(mdic.items(), key=lambda x: x[0])
last = ""
for alpha, cnt in sorted_mdic[::-1]:
    if cnt >= 2:
        answer = alpha* (cnt //2) + answer + alpha * (cnt //2)

    if cnt % 2 == 1:
        if last != "":
            print("I'm Sorry Hansoo")
            flag = False
            break
        last = alpha

answer = answer[:len(answer)//2] + last +  answer[len(answer)//2:]

if flag:
    print(answer)