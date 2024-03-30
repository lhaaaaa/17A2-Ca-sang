# Bài 1: Tính tổng
'''
n = int(input("Nhập vào số n: "))
if n <= 0:
    print("Số không thỏa mãn")
else:
    i = 1 
    S1 = 0
    S2 = 0 
    S3 = 0
    S4 = 0
    S5 = 0
    S6 = 0 
    while i < n + 1:
        S1 = S1 + i**2 
        if i % 2 != 0:
            S2 = S2 + i**3 
        else:
            S3 = S3 + i**4 
        S4 = S4 + ((-1)**(i-1))/i
        S5 = S5 + 1/(i*(i+1))
        if i > 1:
            S6 = S6 + 1/(i**0.5)
        i += 1 
    print("S1 =", S1)
    print("S2 =", S2)
    print("S3 =", S3)
    print("S4 =", S4)
    print("S5 =", S5)
    print("S6 =", S6)
'''

"""
Bài 2: Viết chương trình nhập vào tử số và mẫu số của một phân số, 
kiểm tra mẫu số nhập là số 0 thì nhập lại.
Chương trình in ra phân số đó dưới dạng tối giản.
"""
'''
while True:
    tu_so = int(input("Nhập vào tử số của phân số: "))
    mau_so = int(input("Nhập vào mẫu số của phân số: "))
    if mau_so == 0:
        print("Nhập lại mẫu số")
    if tu_so > mau_so:
        a = tu_so
        b = mau_so
        while b !=0:
            a, b = b, a % b
        tu_so_moi = tu_so / a
        mau_so_moi = mau_so/ a
        print(f"Phân số tối giản là {tu_so_moi}/{mau_so_moi}")
        break
    elif tu_so < mau_so:
        a = tu_so
        b = mau_so
        while a != 0:
            b, a = a, b % a
        tu_so_moi = tu_so / b
        mau_so_moi = mau_so /b
        print(f"Phân số tối giản là {int(tu_so_moi)}/{int(mau_so_moi)}")
        break
    else:
        print("Phân số là: 1")
        break
'''

# Bài 4: Viết chương trình nhập một số từ bàn phím và in ra màn hình bằng chữ
'''
n = int(input("Nhập số từ bàn phím: "))
count = 1
a = n 
while True: #Đếm số lượng chữ số trong số đó
    a = a//10  # lấy phần nguyên
    if a == 0:
        break
    count += 1 

for i in range(count,0,-1):
    phan_nguyen = n//(10**(i-1))
    if phan_nguyen == 0:
        print("không", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 1:
        print("một", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 2:
        print("hai", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 3:
        print("ba", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 4:
        print("bốn", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 5:
        print("năm", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 6:
        print("sáu", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 7:
        print("bảy", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 8:
        print("tám", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 9:
        print("chín", end = " ")
        n = n % (10**(i-1))
'''

"""
Viết chương trình tìm bội chung nhỏ nhất của hai số nguyên được nhập từ bàn phím.
Tìm BCNN thông qua giải thuật Euclide:
+ Tính UCLN của a và b bằng cách sử dụng giải thuật Euclid
+ Sau khi tìm được UCLN(a, b), ta có thể tính BCNN của a và b bằng công thức: 
BCNN(a, b) = (a * b) / UCLN(a, b)
"""
#Tìm UCLN:
m = int(input("Nhập vào số m: "))
n = int(input("Nhập vào số n: "))
if m > n:
    a = m
    b = n
    while b !=0:
        a, b = b, a % b
    ucln = a
else:
    a = m
    b = n
    while a !=0:
        b, a = a, b % a
    ucln = b
#Tìm BCNN
bcnn = (m*n)/ucln
print("BCNN của 2 số là", int(bcnn))




        


