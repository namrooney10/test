def is_palindrome_base(x, k):
    # Đổi x sang cơ số k
    a = []

    while x > 0:
        a.append(x % k)
        x //= k

    # Kiểm tra dãy chữ số có đối xứng không
    return a == a[::-1]


def generate_binary_palindromes(a, b):
    ans = []

    # Số 0 cũng là số thuận nghịch
    if a == 0:
        ans.append(0)

    # Sinh các số thuận nghịch trong cơ số 2
    # Vì b <= 2 * 10^6 nên số chữ số nhị phân không quá 21
    for length in range(1, 22):
        half = (length + 1) // 2

        start = 1 << (half - 1)
        end = 1 << half

        for x in range(start, end):
            s = bin(x)[2:]

            if length % 2 == 0:
                t = s + s[::-1]
            else:
                t = s + s[-2::-1]

            value = int(t, 2)

            if value > b:
                break

            if value >= a:
                ans.append(value)

    return ans


a, b, m = map(int, input().split())

# Chỉ xét những số đã thuận nghịch trong cơ số 2
candidates = generate_binary_palindromes(a, b)

count = 0

for x in candidates:
    ok = True

    # Cơ số 2 đã được đảm bảo.
    # Kiểm tra các cơ số còn lại.
    for k in range(3, min(m, x) + 1):
        if not is_palindrome_base(x, k):
            ok = False
            break

    if ok:
        count += 1

print(count)