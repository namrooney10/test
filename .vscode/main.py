
import sys
input = sys.stdin.readline

t = int(input())
a = [int(input()) for _ in range(t)]
m = max(a)

# Đếm số lượng ước của từng số
uoc = [0] * (m + 1)

for i in range(1, m + 1):
    for j in range(i, m + 1, i):
        uoc[j] += 1

# Đánh dấu các số phản nguyên tố
check = [False] * (m + 1)
max_uoc = 0

for i in range(1, m + 1):
    if uoc[i] > max_uoc:
        check[i] = True
        max_uoc = uoc[i]

# Với mỗi X, tìm số phản nguyên tố nhỏ nhất >= X
ans = [0] * (m + 1)
next_num = 0

for i in range(m, 0, -1):
    if check[i]:
        next_num = i
    ans[i] = next_num

for x in a:
    print(ans[x])
