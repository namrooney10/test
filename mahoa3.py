# Hàm xoay chuỗi
def turn(s):

    # Tính tổng giá trị của các ký tự
    # A có giá trị 0, B = 1, ..., Z = 25
    sum = 0
    for i in s:
        sum += ord(i) - ord('A')

    # Tạo chuỗi sau khi xoay
    r = ''

    for i in s:

        # Giá trị mới của ký tự:
        # (giá trị cũ + tổng) % 26
        r += chr(
            (ord(i) - ord('A') + sum) % 26 + ord('A')
        )

    return r


# Số lượng bộ test
for t in range(int(input())):

    # Nhập chuỗi
    s = input()

    # Chia chuỗi thành 2 nửa
    a = turn(s[:len(s) // 2])
    b = turn(s[len(s) // 2:])

    # Ghép 2 nửa bằng cách cộng từng cặp ký tự
    r = ''

    for i in range(len(a)):

        # Đổi A -> 0, B -> 1, ..., Z -> 25
        # Cộng giá trị của a[i] và b[i]
        # Sau đó % 26 để quay vòng trong A-Z
        r += chr(
            (ord(a[i]) + ord(b[i]) - 2 * ord('A')) % 26
            + ord('A')
        )

    print(r)