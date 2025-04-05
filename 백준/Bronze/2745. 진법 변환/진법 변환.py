import sys

mystr, B = map(str, sys.stdin.readline().rstrip().split())
arr = list(mystr)
arr.reverse()
answer = 0
idx = 1
for i in arr:
    if i.isdecimal():
        answer += int(i) * (int(B) ** (idx-1))
    else:
        answer += (ord(i)-55) * (int(B) ** (idx-1))
    idx += 1

print(answer)
