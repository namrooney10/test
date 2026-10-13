from datetime import date, datetime

# Xây dựng lớp lưu thông tin thể loại
class ob:
    def __init__(self, i, name) -> None:
        # Tạo mã thể loại theo thứ tự TL001, TL002,...
        self.code = f'TL{str(i).zfill(3)}'

        # Lưu tên thể loại
        self.name = name


# Xây dựng lớp lưu thông tin phim, kế thừa từ lớp ob
class ob2(ob):
    def __init__(self, i, type, date, nth, eps) -> None:
        # Tạo mã phim theo thứ tự P001, P002,...
        self.code = f'P{str(i).zfill(3)}'

        # Lưu tên thể loại của phim
        self.type = type

        # Chuyển ngày tháng từ chuỗi sang kiểu datetime để sắp xếp
        self.date = datetime.strptime(date, '%d/%m/%Y')

        # Lưu ngày tháng ban đầu để in ra
        self.strdate = date

        # Lưu thông tin số tập
        self.nth = nth

        # Lưu tên phim
        self.eps = eps

    # Quy định cách in thông tin phim
    def __str__(self) -> str:
        return self.code + ' ' + self.type + ' ' + self.strdate + ' ' + self.nth + ' ' + self.eps


# Nhập số lượng thể loại và số lượng phim
n, m = map(int, input().split())

# Tạo từ điển lưu mã thể loại và tên thể loại
# Tạo danh sách lưu các đối tượng phim
a, arr = {}, []

# Nhập thông tin các thể loại
for i in range(n):
    s = ob(i + 1, input())

    # Lưu tên thể loại tương ứng với mã thể loại
    a[s.code] = s.name

# Nhập thông tin các phim
for i in range(m):
    # Tra cứu mã thể loại để lấy tên thể loại
    # Sau đó tạo đối tượng phim và thêm vào danh sách
    arr.append(ob2(i + 1, a[input()], input(), input(), input()))

# Sắp xếp phim theo ngày phát hành tăng dần rồi in kết quả
for i in sorted(arr, key=lambda x: x.date):
    print(i)