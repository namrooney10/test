t = int(input())

for _ in range(t):
    s = input()

    if len(s) < 3:
        print("NO")
        continue

    phase = 0
    ok = True

    for i in range(1, len(s)):
        if phase == 0:
            if s[i] > s[i-1]:
                continue
            elif s[i] < s[i-1]:
                phase = 1
            else:
                ok =  False
                break

        else:
            if s[i] >= s[i-1]:
                ok = False
                break

    if phase == 0:
        ok = False

    if ok: print("YES")
    else: print("NO")