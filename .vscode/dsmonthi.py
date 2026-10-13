# Xây dựng lớp đối tượng lưu thông tin
class ob:
    def __init__(self, code, name, met) -> None:
        # Lưu mã đối tượng
        self.code = code

        # Lưu tên đối tượng
        self.name = name

        # Lưu thông tin met
        self.met = met

    # Quy định cách in thông tin của đối tượng
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + self.met


# Tạo danh sách lưu các đối tượng
a = []

# Nhập số lượng đối tượng và thông tin của từng đối tượng
for i in range(int(input())):
    a.append(ob(input(), input(), input()))

# Sắp xếp danh sách theo mã tăng dần rồi in kết quả
for i in sorted(a, key=lambda x: x.code):
    print(i)