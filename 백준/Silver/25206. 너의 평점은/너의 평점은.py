import sys

grade_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
answer = 0
cnt = 0

for i in range(20):
    a,b,c = sys.stdin.readline().rstrip().split()

    if c == 'P':
        continue
    cnt = cnt + float(b)

    if c == "A+":
        answer += (grade_list[0]*float(b))
    if c == "A0":
        answer += (grade_list[1]*float(b))
    if c == "B+":
        answer += (grade_list[2]*float(b))
    if c == "B0":
        answer += (grade_list[3]*float(b))
    if c == "C+":
        answer += (grade_list[4]*float(b))
    if c == "C0":
        answer += (grade_list[5]*float(b))
    if c == "D+":
        answer += (grade_list[6]*float(b))
    if c == "D0":
        answer += (grade_list[7]*float(b))
    if c == "F":
        answer += (grade_list[8]*float(b))

print(answer/cnt)