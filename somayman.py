from bisect import bisect_right
t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    # Sắp xếp để dùng binary search tìm vị trí
    a.sort()

    # prefix[i]=tổng a[0]+..+a[i-1]
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]+a[i]

    # Kiểm tra xem có thể tạo x nhóm hay không
    def check(x):
        # Tìm số phần tử <= x
        pos = bisect_right(a,x)

        # Các nước có a[i]<=x:
        # dùng toàn bộ a[i] người
        tong = prefix[pos]

        # Các nước có a[i]>x:
        # mỗi nước chỉ đóng góp tối đa x người
        tong += (n-pos)*x

        # Cần đủ x * k người để tạo x nhóm
        return tong >= x*k

    # Số nhóm ko thể vượt quá tổng số người / k
    l = 0
    r = prefix[n]//k
    ans = 0

    # Binary search tìm số nhóm lớn nhất
    while l<=r:
        mid = (l+r)//2
        if check(mid):
            # Tạo được mid nhóm:
            ans = mid
            l = mid+1
        else:
            # mid quá lớn
            r = mid-1

    print(ans)
