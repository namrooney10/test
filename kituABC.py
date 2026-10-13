n = int(input())

ans=[]

# Sinh các xâu có độ dài len
def backtrack(s,length, a,b,c):
    # Nếu đã đủ độ dài
    if len(s) == length:
        # Phải chứa cả A,B,C
        # và số A <= B <= C
        if a > 0 and b > 0 and c > 0 and a<=b<=c:
            ans.append(s)
        return

    # Thêm A
    backtrack(s+'A',length,a+1,b,c)

    # Thêm B
    backtrack(s+'B',length,a,b+1,c)

    # Thêm C
    backtrack(s+'C',length,a,b,c+1)

# Sinh lần lượt độ dài từ 3 đến N
for length in range(3, n+1):
    backtrack('',length,0,0,0)

print('\n'.join(ans))