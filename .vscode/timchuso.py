# Modulo dùng để giới hạn giá trị trong khoảng từ 0 đến 999
mod = 1000


# Xây dựng lớp lưu một cặp số (x, y)
class pair:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # Quy định cách in cặp số
    def __str__(self) -> str:
        return f'{self.x} {self.y}'


# Nhân hai cặp số theo công thức của bài toán
def mul(a, b):
    r = pair(0, 0)

    # Tính thành phần thứ nhất và lấy phần dư cho mod
    r.x = (a.x * b.x + 5 * a.y * b.y) % mod

    # Tính thành phần thứ hai và lấy phần dư cho mod
    r.y = (a.x * b.y + a.y * b.x) % mod

    return r


# Tính lũy thừa của cặp số bằng thuật toán lũy thừa nhanh
def pow(a, b):
    # Trường hợp số mũ bằng 0, kết quả là (1, 0)
    if b == 0:
        return pair(1, 0)

    # Nếu số mũ lẻ, giảm số mũ đi 1 rồi nhân với a
    if b & 1:
        return mul(pow(a, b - 1), a)

    # Nếu số mũ chẵn, tính a^(b/2) rồi bình phương kết quả
    p = pow(a, b >> 1)
    return mul(p, p)


# Khởi tạo cặp số ban đầu (3, 1)
x = pair(3, 1)

# Nhập số lượng bộ test và xử lý từng bộ test
for t in range(int(input())):
    print(f'Case #{t + 1}: ', end='')

    # Tính lũy thừa của cặp số x với số mũ nhập vào
    # Lấy thành phần x, nhân 2, trừ 1 rồi lấy phần dư mod 1000
    # In kết quả đủ 3 chữ số, thêm số 0 ở đầu nếu cần
    print(str(pow(x, int(input())).x * 2 % mod - 1).zfill(3))