
month, day = map(int, input().split())

month_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
tmp = 0
for i in range(month):
    tmp += month_list[i]

tmp += day

if tmp % 7 == 1:
    print("MON")
elif tmp % 7 == 2:
    print("TUE")
elif tmp % 7 == 3:
    print("WED")
elif tmp % 7 == 4:
    print("THU")
elif tmp % 7 == 5:
    print("FRI")
elif tmp % 7 == 6:
    print("SAT")
elif tmp % 7 == 0:
    print("SUN")
