# Tìm vị trí j thích hợp để đổi với s[i]
def mind(s, i):
    ans = i

    # Duyệt các vị trí phía sau i
    for j in range(i + 1, len(s)):

        # Chỉ xét chữ số nhỏ hơn s[i]
        if s[j] < s[i]:

            # Lần đầu tiên tìm được chữ số nhỏ hơn s[i]
            if ans == i:
                ans = j

            # Nếu đã có một vị trí trước đó,
            # chọn chữ số lớn hơn trong các chữ số nhỏ hơn s[i]
            elif s[ans] < s[j]:
                ans = j

    # Nếu tìm được chữ số nhỏ hơn s[i]
    if s[ans] < s[i]:
        return ans

    # Không tìm được
    return -1


# Số lượng bộ test
for t in range(int(input())):

    # Nhập số dưới dạng chuỗi
    s = input()
    n = len(s)

    # Lưu kết quả
    ans = ''

    # Duyệt từ phải sang trái
    for i in range(n - 1, -1, -1):

        # Tìm vị trí chữ số thích hợp để đổi với s[i]
        ind = mind(s, i)

        # Nếu tìm được
        if ind > -1:

            # Đổi s[i] và s[ind]
            ans = s[:i] + s[ind] + s[i + 1:ind] + s[i] + s[ind + 1:]

            # Chỉ cần đổi một lần nên dừng lại
            break

    # Kiểm tra kết quả:
    # - ans khác rỗng
    # - ans khác số ban đầu
    # - chữ số đầu tiên không được là 0
    if ans != '' and ans != s and ans[0] != '0':
        print(ans)
    else:
        print('-1')