# Nhập số lượng dòng
a = []

for i in range(int(input())):
    a.append(input())

# Xử lý từng nhóm dữ liệu
while len(a) > 0:

    # Mặc định vị trí dòng rỗng là cuối danh sách
    ind = len(a)

    # Tìm dòng rỗng đầu tiên
    for i in range(len(a)):
        if a[i] == '':
            ind = i
            break

    # Dòng đầu tiên là tên/tiêu đề của nhóm
    # Các dòng từ 1 đến ind-1 là dữ liệu của nhóm
    print(f'{a[0]}: {ind - 1}')

    # Xóa nhóm vừa xử lý:
    # a[0] là tên nhóm
    # a[1] ... a[ind-1] là dữ liệu
    # a[ind] là dòng rỗng
    a = a[ind + 1:]