a, b, m = map(int, input().split())

# Nếu m > 3 thì chỉ cần xét 0 và 1
if m > 3:
    cnt = 0

    for i in [0, 1]:
        if a <= i and i <= b:
            cnt += 1

    print(cnt)


# Nếu m = 3
elif m == 3:
    cnt = 0

    # Các số đối xứng nhị phân cần xét
    for i in [0, 1, 6643, 1422773, 5415589]:
        if a <= i and i <= b:
            cnt += 1

    print(cnt)


# Nếu m = 2
elif m == 2:
    cnt = 0

    # Sinh các chuỗi nhị phân đối xứng
    for i in range(1, 10000):

        # Chuyển i sang dạng nhị phân và bỏ tiền tố '0b'
        s1 = bin(i)[2:]

        # Đảo ngược chuỗi nhị phân
        s2 = ''.join(reversed(s1))

        # Tạo 3 dạng số đối xứng:
        # 1. s1 + s2
        # 2. s1 + '0' + s2
        # 3. s1 + '1' + s2
        arr = [
            s1 + s2,
            s1 + '0' + s2,
            s1 + '1' + s2
        ]

        # Duyệt 3 số vừa tạo
        for j in arr:

            # Chuyển chuỗi nhị phân về số nguyên
            x = int(j, 2)

            # Kiểm tra x có nằm trong [a, b] không
            if a <= x and x <= b:
                cnt += 1

    # Bổ sung hai số đặc biệt 0 và 1
    for i in [0, 1]:
        if a <= i and i <= b:
            cnt += 1

    print(cnt)


# Các trường hợp còn lại
else:
    print(0)