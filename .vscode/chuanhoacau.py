# Khởi tạo chuỗi lưu toàn bộ văn bản
doc = ''

# Đọc dữ liệu cho đến khi hết dữ liệu đầu vào
while True:
    try:
        doc += input()

        # Nếu cuối dòng chưa có dấu kết thúc câu thì thêm dấu chấm
        if doc[-1] not in '.?!':
            doc += ' .'
        else:
            # Nếu trước dấu kết thúc câu không có dấu cách thì thêm dấu cách
            if doc[-2] != ' ':
                doc = f'{doc[:-1]} {doc[-1]}'

        # Thêm dấu cách để phân tách các dòng
        doc += ' '

    except:
        # Dừng khi không còn dữ liệu đầu vào
        break


# Tách văn bản thành danh sách các từ
words = doc.split()

# Khởi tạo chỉ số duyệt danh sách từ
i = 0

# Duyệt lần lượt các từ để ghép thành từng câu
while i < len(words):
    sen = ''

    # Ghép các từ cho đến khi gặp dấu kết thúc câu
    while i < len(words) and words[i] not in '.?!':
        sen += words[i] + ' '
        i += 1

    # Nếu gặp dấu kết thúc câu thì ghép dấu vào cuối câu
    if words[i] in '.?!':
        sen = sen[:-1] + words[i]

    # Chuyển sang từ tiếp theo sau dấu kết thúc câu
    i += 1

    # Viết hoa chữ cái đầu câu, chuyển các chữ còn lại thành chữ thường
    print(sen[0].upper() + sen[1:].lower())