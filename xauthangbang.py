# Số lượng bộ test
for t in range(int(input())):

    # Hàm kiểm tra chuỗi
    def c(s):

        # Tạo chuỗi đảo ngược của s
        rs = ''.join(reversed(s))

        # Duyệt từng cặp ký tự liên tiếp
        for i in range(1, len(s)):

            # Độ chênh lệch giữa 2 ký tự trong chuỗi ban đầu
            a = abs(ord(s[i]) - ord(s[i - 1]))

            # Độ chênh lệch giữa 2 ký tự trong chuỗi đảo ngược
            b = abs(ord(rs[i]) - ord(rs[i - 1]))

            # Nếu 2 độ chênh lệch khác nhau
            # thì chuỗi không thỏa mãn
            if a != b:
                return 'NO'

        # Tất cả các cặp ký tự đều thỏa mãn
        return 'YES'

    # Nhập chuỗi và kiểm tra
    print(c(input()))