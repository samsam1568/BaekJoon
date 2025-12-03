import sys

my_dic = dict()

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
for i in arr:
    if int(i) in my_dic:
        my_dic[i] += 1
    else:
        my_dic[i] = 1

my_dic = sorted(my_dic.items(), key = lambda x: (-x[1], x[0]))

print(my_dic[0][0])