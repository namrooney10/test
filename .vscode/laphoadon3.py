# Xây dựng lớp đối tượng lưu thông tin sản phẩm
class ob:
    def __init__(self, code, name, num, price, ck) -> None:
        # Lưu mã sản phẩm
        self.code = code

        # Lưu tên sản phẩm
        self.name = name

        # Lưu số lượng sản phẩm
        self.num = num

        # Lưu đơn giá sản phẩm
        self.price = price

        # Lưu số tiền chiết khấu
        self.ck = ck

        # Tính tổng tiền sau khi trừ chiết khấu
        self.sum = num * price - ck

    # Quy định cách in thông tin của một sản phẩm
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + str(self.num) + ' ' + str(self.price) + ' ' + str(self.ck) + ' ' + str(self.sum)


# Tạo danh sách lưu các đối tượng sản phẩm
a = []

# Nhập số lượng sản phẩm và thông tin của từng sản phẩm
for i in range(int(input())):
    a.append(ob(input(), input(), int(input()), int(input()), int(input())))

# Sắp xếp sản phẩm theo tổng tiền giảm dần và in kết quả
for i in sorted(a, key=lambda x: -x.sum):
    print(i)