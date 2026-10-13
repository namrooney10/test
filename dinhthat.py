# Kiểm tra xem sau khi bỏ đỉnh e,
# còn đường đi từ u đến v hay không
def check(ke, u, v, e, n):

    # Bắt đầu DFS từ u
    q = [u]

    # Mảng đánh dấu các đỉnh đã thăm
    un = [0] * (n + 1)
    un[u] = 1

    while len(q) > 0:

        # Lấy một đỉnh ra khỏi ngăn xếp
        x = q.pop()

        # Nếu đi được đến v
        # thì vẫn còn đường từ u đến v
        if x == v:
            return False

        # Duyệt các đỉnh kề với x
        for i in ke[x]:

            # Chưa thăm và không phải đỉnh e bị xóa
            if un[i] == 0 and i != e:
                q.append(i)
                un[i] = 1

    # Không đi được đến v
    # => xóa e làm mất đường đi từ u đến v
    return True


# Số lượng bộ test
for t in range(int(input())):

    # n: số đỉnh
    # m: số cạnh
    # u, v: hai đỉnh cần kiểm tra đường đi
    n, m, u, v = map(int, input().split())

    # Danh sách kề
    ke = {x: [] for x in range(1, n + 1)}

    # Nhập các cạnh
    for i in range(m):
        x, y = map(int, input().split())
        ke[x].append(y)

    cnt = 0

    # Thử xóa từng đỉnh
    for i in range(n + 1):

        # Không được xóa u hoặc v
        if i != u and i != v:

            # Kiểm tra xem sau khi xóa i,
            # u còn đi được đến v không
            if check(ke, u, v, i, n):
                cnt += 1

    # In số đỉnh mà khi xóa nó sẽ làm mất đường đi u -> v
    print(cnt)