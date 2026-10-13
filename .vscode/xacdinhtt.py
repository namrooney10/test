# Xác định môn học dựa vào ký tự đầu tiên của mã xét tuyển
def sub(s):
    if s[0] == 'A':
        return 'TOAN'
    if s[0] == 'B':
        return 'LY'
    return 'HOA'


# Xác định điểm ưu tiên dựa vào ký tự thứ hai của mã xét tuyển
def sup(s):
    if s[1] == '1':
        return 2
    if s[1] == '2':
        return 1.5
    if s[1] == '3':
        return 1
    return 0


# Xây dựng lớp đối tượng giáo viên
class ob:
    def __init__(self, i, name, code, t, c) -> None:
        # Tạo mã giáo viên theo thứ tự, gồm 2 chữ số
        self.code = f'GV{str(i).zfill(2)}'

        # Lưu họ tên giáo viên
        self.name = name

        # Xác định môn học từ mã xét tuyển
        self.sub = sub(code)

        # Tính tổng điểm: điểm ưu tiên + điểm thi chính * 2 + điểm thi phụ
        self.sum = sup(code) + t * 2 + c

        # Xác định kết quả tuyển sinh
        if self.sum >= 18:
            self.type = 'TRUNG TUYEN'
        else:
            self.type = 'LOAI'

    # Quy định cách chuyển đối tượng thành chuỗi để in ra
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + self.sub + ' ' + f'{self.sum:.1f}' + ' ' + self.type


# Tạo danh sách lưu các đối tượng giáo viên
a = []

# Nhập số lượng giáo viên và thông tin của từng người
for i in range(int(input())):
    a.append(ob(i + 1, input(), input(), float(input()), float(input())))

# Sắp xếp danh sách theo tổng điểm giảm dần và in kết quả
for i in sorted(a, key=lambda x: -x.sum):
    print(i)