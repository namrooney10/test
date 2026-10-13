# Nhập số lượng bộ test
for t in range(int(input())):

    # Chuyển chuỗi thứ nhất thành danh sách các ký tự
    a = [i for i in input()]

    # Chuyển chuỗi thứ hai thành danh sách các ký tự
    b = [i for i in input()]

    # Sắp xếp 2 danh sách rồi so sánh
    # Nếu giống nhau => 2 chuỗi có cùng các ký tự với cùng số lần xuất hiện
    if sorted(a) == sorted(b):
        print(f'Test {t + 1}: YES')
    else:
        print(f'Test {t + 1}: NO')