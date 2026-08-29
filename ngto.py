import math

def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

def tcs(n):
    tong  = 0
    while n > 0:
        a = n % 10
        tong += a
        n //= 10

    return tong

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    c = math.gcd(a, b)

    if ngto(tcs(c)): print("YES")
    else: print("NO")
    print()  