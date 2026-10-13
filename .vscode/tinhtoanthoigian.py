from datetime import datetime

# Xây dựng lớp đối tượng lưu thông tin nhân viên
class per:
    def __init__(self, code, name, tin, tout) -> None:
        # Lưu mã nhân viên
        self.code = code

        # Lưu họ tên nhân viên
        self.name = name

        # Tính thời gian làm việc bằng giờ vào và giờ ra
        # Chuyển chuỗi giờ phút thành kiểu datetime rồi lấy hiệu
        self.time = datetime.strptime(tout, '%H:%M') - datetime.strptime(tin, '%H:%M')


# Tạo danh sách lưu các đối tượng nhân viên
a = []

# Nhập số lượng nhân viên và thông tin của từng người
for i in range(int(input())):
    a.append(per(input(), input(), input(), input()))

# Sắp xếp nhân viên theo thời gian làm việc giảm dần
a.sort(key=lambda x: -x.time)

# In mã nhân viên, họ tên và thời gian làm việc
for i in a:
    print(i.code, i.name, i.time.seconds // 3600, 'gio', i.time.seconds // 60 % 60, 'phut')