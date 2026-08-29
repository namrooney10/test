P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    a = input().split()

    if a[0]=='0':
        break

    k = int(a[0])
    s = a[1]
    res = ""
    for c in s:
        pos = P.index(c)
        res += P[(pos+k)%28]

    print(res[::-1]) 