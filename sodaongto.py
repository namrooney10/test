import math

t = int(input())

for _ in range(t):
    s = input()
    a = int(s)
    b = int(s[::-1])

    if math.gcd(a, b) == 1:
        print("YES")
    else:
        print("NO")