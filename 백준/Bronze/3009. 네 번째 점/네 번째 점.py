XDic = dict()
YDic = dict()

for _ in range(3):
    a,b = map(int,input().split())
    if a in XDic:
        XDic[a] += 1
    elif a not in XDic:
        XDic[a] = 1

    if b in YDic:
        YDic[b] += 1

    elif b not in YDic:
        YDic[b] = 1

x = sorted(XDic.items(), key=lambda x: x[1])
y = sorted(YDic.items(), key=lambda x: x[1])

print(x[0][0],y[0][0])