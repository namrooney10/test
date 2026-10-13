t = int(input())

for _ in range(t):
    b = int(input())
    s = input().strip()

    # Số bit tạo thành 1 chữ số trong cơ số b
    k = 1
    if b == 4:
        k = 2
    elif b == 8:
        k = 3
    elif b == 16:
        k = 4

    # Thêm số 0 vào đầu nếu chưa đủ nhóm
    while len(s) % k != 0:
        s = '0' + s

    ans = ""

    for i in range(0, len(s), k):
        group = s[i:i + k]

        # Đổi nhóm bit sang số
        value = int(group, 2)

        if value < 10:
            ans += str(value)
        else:
            ans += chr(value-10 + ord('A'))

    ans = ans.lstrip('0')

    if ans == "":
        ans = "0"
    print(ans)