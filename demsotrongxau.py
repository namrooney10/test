# Số lượng bộ test
for t in range(int(input())):

    # s: chuỗi lớn
    # n: chuỗi cần tìm
    s, n = input(), input()

    # Độ dài của 2 chuỗi
    l1, l2 = len(s), len(n)

    # cnt: số lần tìm thấy n
    # i: vị trí hiện tại đang xét trong s
    cnt = i = 0

    # Duyệt từ đầu đến cuối chuỗi s
    while i < l1:

        # Lấy một đoạn có độ dài bằng n
        # bắt đầu từ vị trí i
        if s[i:i + l2] == n:

            # Tìm thấy n
            cnt += 1

            # Bỏ qua toàn bộ đoạn vừa tìm được
            # để không đếm chồng lên nhau
            i += l2

        else:
            # Không tìm thấy, dịch sang vị trí tiếp theo
            i += 1

    # In số lần xuất hiện
    print(cnt)