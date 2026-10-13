# Chuẩn hóa tên: viết hoa chữ cái đầu, các chữ còn lại viết thường
def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()])


# Xây dựng lớp lưu thông tin đội thi
class ob:
    def __init__(self, i, name, school) -> None:
        # Tạo mã đội theo thứ tự Team01, Team02,...
        self.code = f'Team{str(i).zfill(2)}'

        # Lưu tên đội
        self.name = name

        # Lưu tên trường
        self.school = school


# Xây dựng lớp lưu thông tin thí sinh
class ob2:
    def __init__(self, i, name, o) -> None:
        # Tạo mã thí sinh theo thứ tự C001, C002,...
        self.code = f'C{str(i).zfill(3)}'

        # Lưu tên thí sinh
        self.name = name

        # Lưu đối tượng đội thi mà thí sinh tham gia
        self.o = o

    # Quy định cách in thông tin thí sinh
    def __str__(self) -> str:
        return self.code + '  ' + self.name + ' ' + self.o.name + ' ' + self.o.school


# Tạo từ điển lưu thông tin các đội thi theo mã đội
team = {}

# Nhập thông tin các đội thi
for i in range(int(input())):
    o = ob(i + 1, input(), input())

    # Lưu đối tượng đội thi vào từ điển
    team[o.code] = o


# Tạo danh sách lưu thông tin các thí sinh
a = []

# Nhập thông tin thí sinh và mã đội mà thí sinh tham gia
for i in range(int(input())):
    a.append(ob2(i + 1, input(), team[input()]))

# Sắp xếp thí sinh theo tên tăng dần rồi in kết quả
for i in sorted(a, key=lambda x: x.name):
    print(i)