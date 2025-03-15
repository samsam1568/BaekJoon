import sys

T = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split()))
B = list(map(int,sys.stdin.readline().rstrip().split()))

A.sort(reverse=True)
z = B.copy()
z.sort()

tmp = 0
for i in range(T):
    tmp += A[i]*z[i]
print(tmp)

# [1,3,5,7,9]
#
# [2,7,8,3,1]
# =>
# 1,2,3,7,8 매칭
#
# 매칭된 value에 해당하는 idx값을 가져옴
