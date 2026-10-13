from sys import stdin

# Dùng stdin.readline() để nhập dữ liệu nhanh hơn
# stdin = open('D:/code/in.txt')

n, k, tmp, a, b = 0, 0, 0, [], []


# Kiểm tra xem giá trị g có thể đạt được hay không
def check(g):

    # Tìm vị trí đầu tiên trong a có giá trị >= g
    l, r = 0, n

    while l < r:
        mid = (l + r) >> 1

        if a[mid] < g:
            l = mid + 1
        else:
            r = mid

    # b[l-1] là tổng các phần tử nhỏ hơn g
    # Kiểm tra tổng đó có đủ lớn hay không
    return b[l - 1] >= g * (l + tmp)


# Số lượng bộ test
for t in range(int(stdin.readline())):

    # Nhập n và k
    n, k = map(int, stdin.readline().split())

    # Đọc mảng và sắp xếp tăng dần
    a = sorted(map(int, stdin.readline().split()))

    # Tạo mảng prefix sum
    b = a.copy()

    # b[i] = a[0] + a[1] + ... + a[i]
    for i in range(1, n):
        b[i] += b[i - 1]

    # Nếu số phần tử ít hơn k
    # thì không thể thực hiện được
    if n < k:
        print(0)
        continue

    # Nếu n = k thì đáp án chính là phần tử nhỏ nhất
    if n == k:
        print(a[0])
        continue

    # tmp = k - n
    tmp = k - n

    # Tìm đáp án bằng tìm kiếm nhị phân
    l, r = 0, sum(a) // k

    while l < r:

        # Tính giá trị giữa
        mid = (l + r) >> 1

        # Nếu mid thỏa mãn
        # thì thử tìm giá trị lớn hơn
        if check(mid):
            l = mid + 1

        # Nếu không thỏa mãn
        # thì giảm phạm vi tìm kiếm
        else:
            r = mid

    # Kiểm tra lại giá trị l
    if check(l):
        print(l)
    else:
        print(l - 1)