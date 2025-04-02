import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = list(sys.stdin.readline().rstrip())
    m = len(n)
    for j in range(m):
        if n[j] == "Z":
            n[j] = "A"
        else:
            n[j] = chr(ord(n[j])+1)
    print("String #%d" % (i + 1))
    for s in range(m):
        print(n[s], end = "")
    print()
    if i == T - 1:
        break
    print()