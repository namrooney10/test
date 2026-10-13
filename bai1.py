n = int(input())

ds=[]

for i in range(n):
    ma = input()
    ten = input()
    lop = input()
    ds.append([ma,ten,lop])

diem_danh = {}

for i in range(n):
    s = input().split()
    ma = s[0]
    trang_thai = s[1]

    diem = 10

    for c in trang_thai:
        if c == 'm':
            diem -= 1
        elif c == 'v':
            diem -= 2

    if diem < 0:
        diem = 0

    diem_danh[ma] = diem

for ma, ten, lop in ds:
    diem = diem_danh[ma]

    print(ma, ten, lop, diem, end=' ')

    if diem == 0:
        print(" KDDK")
    else:
        print()