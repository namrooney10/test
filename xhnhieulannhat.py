t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dem = {}

    # Đếm số lần xuất hiện
    for x in a:
        if x in dem:
            dem[x] += 1
        else:
            dem[x] = 1

    ans = -1

    # Tìm số xuất hiện > N/2 lần
    for x in dem:
        if dem[x] > n / 2:
            if ans == -1 or x < ans:
                ans = x

    if ans == -1:
        print("NO")
    else:
        print(ans)