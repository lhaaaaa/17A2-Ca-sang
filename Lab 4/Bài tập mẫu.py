# Bài 1: Viết chương trình để in các số từ 1 đến 10
#a = 1 
#print("In ra các số từ 1 đến 10:")
#while a < 11:
#    print(a, end =" ") # In ra các số theo hàng ngang
#    a += 1

"""
Bài 2:
Viết chương trình tìm ước chung lớn nhất (UCLN) của 2 số nguyên m và n.
Sử dụng thuật toán Euclid
"""
#m = int(input("Nhập vào số m: "))
#n = int(input("Nhập vào số n (n < m): "))
#while n!=0:
#    m, n = n, m % n
#print(f"UCLN của 2 số là: {m}")

"""
Ví dụ: Với m = 8, n = 6
Vòng lặp 1: 6 khác 0 -> chạy khối lệnh
    m = 6 
    n = 2
Vòng lặp 2: 2 khác 0 -> chạy khối lệnh
    m = 2
    n = 0
n = 0 -> Điều kiện trong while trở False -> vòng lặp dừng
""" 

# Bài 4: Viết chương trình nhập số n. Chương trình sẽ kết thúc nếu một trong các số đó là số âm
"""
Hướng dẫn:
Điều kiện vòng lặp: số nhập vào là số âm
Khối lệnh bên trong vòng lặp: nhập số từ bàn phím và in ra số đó
"""

"""
Bài 5:
Viết chương trình nhập vào một số nguyên và in kết quả ra màn hình dưới dạng số đảo ngược
(về thứ tự) của số nguyên vừa nhập đó.
Ví dụ: 123 -> 321
Bước 0: Số ban đầu n = 123 
Bước 1: Gán số đảo ngược = 0
Thực hiện vòng lặp:
Vòng lặp 1:
Bước 1: Thực hiện tính phần dư của 123 cho 10: phần dư = 3 
Bước 2: số đảo ngược = (số đảo ngược * 10) + phần dư = 3 
Bước 3: thực hiện tính phần nguyên của 123 cho 10 và gán vào số ban đầu: n = 12
Điều kiện dừng: Tiếp tục làm như vậy đến khi n <= 0
Vòng lặp 2:
Bước 1: phần dư = 2 
Bước 2: số đảo ngược = 30 + 2 = 32
Bước 3: n = 12//10 = 1
Vòng lặp 3:
Bước 1: phần dư = 1
Bước 2: số đảo ngược = 320 + 1 = 321
Bước 3: n = 1//10 = 0
-> In ra số đảo ngược
"""
#so_ban_dau = int(input("Nhập vào số ban đầu: "))
#so_dao_nguoc = 0 
#while so_ban_dau > 0:
#    phan_du = so_ban_dau % 10
#    so_dao_nguoc = so_dao_nguoc * 10 + phan_du
#    so_ban_dau = so_ban_dau // 10
#print("Số đảo ngược của số ban đầu là:", so_dao_nguoc)

# Bài 6: Viết chương trình kiểm tra một số n có là số nguyên tố
#n = int(input("Nhập vào số nguyên tố: "))
#if n <= 1:
#    print("Vui lòng nhập lại")
#else:
#    a = 2 
#    while a**2 <= n:
#        check = True 
#        if n % a == 0:
#            check = False
#            break
#        a += 1

#    if check == True:
#        print(f"{n} là số nguyên tố")
#    else:
#        print(f"{n} không phải là số nguyên tố")

"""
Bài 7:
Viết chương trình hiển thị một menu các chức năng của phép toán (cộng, trừ, nhân, chia) 
cho người dùng chọn, bấm số 0 để thoát.
"""
'''
a, b = map(int, input("Nhập vào hai số a và b: ").split())
print(
"""
Chương trình hiển thị menu chọn phép toán:
1. Phép cộng 2 số
2. Phép trừ 2 số
3. Phép nhân 2 số
4. Phép chia 2 số
0. Thoát chương trình
"""
)
lua_chon = int(input("Nhập vào lựa chọn: "))
while True:
    if lua_chon == 1:
        print(f"Tổng 2 số là: {a} + {b} = {a + b}")
        break
    elif lua_chon == 2:
        print(f"Hiệu 2 số là: {a} - {b} = {a - b}")
        break
    elif lua_chon == 3:
        print(f"Tích 2 số là: {a} x {b} = {a * b}")
        break
    elif lua_chon == 4:
        print(f"Thương 2 số là: {a} : {b} = {a / b}")
        break
    elif lua_chon == 0:
        break
    else:
        print("Lựa chọn sai, vui lòng nhập lại")
'''

"""
Bài 9: Viết chương trình nhập ID và password
Chương trình sẽ lặp lại việc nhập ID và password cho đến khi user nhập đúng. 
Thao tác nhập được thực hiện ít nhất 1 lần.
"""
'''
id_goc = 'helloabc'
password_goc = 'Abc1234'
while True:
    id = input("Nhập vào ID: ")
    password = input("Nhập vào password: ")
    if id == id_goc and password == password_goc:
        print("Chương trình nhập đúng mật khẩu")
        break
    else:
        print("Vui lòng nhập lại id và password")
'''
# Bài 10: Viết chương trình in tất cả các số nguyên tố từ 1 đến n được nhập từ bàn phím.
'''
n = int(input("Nhập vào số nguyên n: "))
a = 0
i = 2 
while a < n:
    if a <= 1:
        a += 1
    else:
        check = True
        while i < a:
            if a % i == 0:
                check = False
            i += 1
        if check == True:
            print(a, end = ' ')
            a += 1 
        else:
            a += 1
'''
