t = int(input())

for _ in range(t):
    s1 = input()
    s2 = s1[::-1]

    ok = True
    for i in range(1, len(s1)):
        a = abs(ord(s1[i])-ord(s1[i-1]))
        b = abs(ord(s2[i])-ord(s2[i-1]))

        if a != b:
            ok = False
            break

    if ok: print("YES")
    else: print("NO")
