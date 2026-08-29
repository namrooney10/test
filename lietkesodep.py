t = int(input())

for _ in range(t):
    n = int(input())

    for a in "2468":
        s = a+a
        if int(s)<n:
            print(s, end=" ")

    for a in "2468":
        for b in "02468":
            s = a+b+b+a
            if int(s)<n:
                print(s, end=" ")

    for a in "2468":
        for b in "02468":
            for c in "02468":
                s = a+b+c+c+b+a
                if int(s)<n:
                    print(s, end=" ")

    print()