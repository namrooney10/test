# Nhập số hàng và số cột
n, m = map(int, input().split())

# Xác định hướng cần bỏ qua:
# n > m  -> start = 0
# n < m  -> start = 1
# n = m  -> start = -1
start = 0 if n > m else (1 if n < m else -1)


# Xác định giới hạn wall
wall = start + (abs(n - m) - 1) * 2


# Duyệt từng hàng
for i in range(n):

    # Nhập hàng thứ i
    a = input().split()

    # Trường hợp n > m:
    # Bỏ qua các hàng có chỉ số chẵn
    # trong phạm vi wall
    if start == 0 and i % 2 == 0 and i <= wall:
        continue

    # Duyệt từng phần tử trong hàng
    for j in range(m):

        # Trường hợp n < m:
        # Bỏ qua các cột có chỉ số lẻ
        # trong phạm vi wall
        if start == 1 and j % 2 == 1 and j <= wall:
            continue

        # In phần tử
        print(a[j], end=' ')

    print('')