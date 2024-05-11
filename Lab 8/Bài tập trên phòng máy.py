"""
Bài 1:
Viết chương trình để in ra màn hình số kể tiếp của số nguyên 
được người dùng nhập vào từ bàn phím.

def value(x): #x là tham số để tìm số tiếp theo
    y = x + 1
    print(f"Số tiếp theo của {x} là {y}")

x = int(input("Nhập vào một số: "))
value(x)
"""

"""
Bài 2: 
a) Viết chương trình tìm ước chung lớn nhất của 2 số a, b.
b) Xây chương trình tìm bội chung nhỏ nhất của 2 số a, b.
c) Viết chương trình cho phép thực hiện rút gọn phân số.
Hướng dẫn:
+ Tìm UCLN của tử số và mẫu số.
+ Chia tử và mẫu của phân số cho UCLN vừa tìm được.
d) Viết chương trình nhập 3 số nguyên và sau đó in các số nhỏ nhất 
và lớn nhất bởi sử dụng hàm.

# Hàm tìm ước chung lớn nhất
def uoc_chung_lon_nhat(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm tìm bội chung nhỏ nhất
def boi_chung_nho_nhat(a,b):
    ucln = uoc_chung_lon_nhat(a,b)
    bcnn = abs(a*b)//ucln
    return bcnn

# Hàm rút gọn phân số
def rut_gon(a,b):
    ucln = uoc_chung_lon_nhat(a,b)
    tu_so_moi = a//ucln
    mau_so_moi = b//ucln
    return tu_so_moi, mau_so_moi

num1 = 24
num2 = 36
ucln = uoc_chung_lon_nhat(num1, num2)
print("Ước chung lớn nhất của 2 số là", ucln)
bcnn = boi_chung_nho_nhat(num1, num2)
print("Bội chung nhỏ nhất của hai số là", bcnn)
tu_so, mau_so = rut_gon(num1, num2)
print(f"Phân số {num1}/{num2} sau khi rút gọn là {tu_so}/{mau_so}")


# Hàm tìm số lớn nhất
def so_lon_nhat(a,b,c):
    max = a 
    if max < b:
        max = b
    if max < c:
        max = c 
    return max
        
# Hàm tìm số nhỏ nhất
def so_nho_nhat(a,b,c):
    min = a 
    if min > c:
        min = c
    if min > b:
        min = b 
    return min

a, b, c = map(int, input("Nhập vào 3 số a, b, c: ").split())
min_3_so = so_nho_nhat(a,b,c)
max_3_so = so_lon_nhat(a,b,c)
print("Số lớn nhất và số nhỏ nhất trong 3 số là:", max_3_so, ",", min_3_so)
"""

"""
Bài 5: 
Viết chương trình nhập từ 
bàn phím số nguyên dương n và in ra màn hình các ước số của n.

def uoc_so(n):
    uoc = set()
    for i in range(1, n+1):
        if n % i == 0:
            uoc.add(i)
    return uoc

n = int(input("Nhập một số từ bàn phím: "))
tap_uoc_cua_n = uoc_so(n)
print(f"Tập các ước của số {n} là {tap_uoc_cua_n}")
"""

"""
Bài 6: 
Viết chương trình nhập Họ tên, điểm Toán, điểm Lý, điểm Hóa 
của một sinh viên. 
Tính điểm trung bình và xuất ra kết quả.
(Yêu cầu: Viết hàm nhập, xuất, tính trung bình).

def nhap_thong_tin():
    while True:
        ho_ten = input("Nhập họ tên của sinh viên (Nhấn phím q để thoát): ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hóa: "))
        return ho_ten, diem_toan, diem_ly, diem_hoa
    
def tinh_trung_binh(diem_toan, diem_ly, diem_hoa):
    trung_binh = (diem_toan + diem_ly + diem_hoa)/3
    return trung_binh

def in_thong_tin(ho_ten, diem_toan, diem_ly, diem_hoa, diem_trung_binh):
    print("Thông tin của sinh viên là:")
    print("Họ tên:", ho_ten)
    print("Điểm 3 môn Toán, Lý, Hóa:", diem_toan, diem_ly, diem_hoa)
    print("Điểm trung bình 3 môn:", diem_trung_binh)

# Chạy chương trình
# ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin()
#diem_trung_binh = tinh_trung_binh(diem_toan, diem_ly, diem_hoa)
#in_thong_tin(ho_ten, diem_toan, diem_ly, diem_hoa, diem_trung_binh)

# Hàm chạy chương trình
def main():
    ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin()
    diem_trung_binh = tinh_trung_binh(diem_toan, diem_ly, diem_hoa)
    in_thong_tin(ho_ten, diem_toan, diem_ly, diem_hoa, diem_trung_binh)

if __name__ == "__main__":
    main()
"""

"""
Bài 9: 
Viết chương trình thực hiện các yêu cầu sau:
+ Tạo một list có n phần tử là số nguyên được nhập từ bàn phím.
+ Sử dụng map, lambda: Tạo một list chứa bình phương của các số hạng thuộc list trên

n = int(input("Nhập một số từ bàn phím: "))
lst = []
i = 0
while i < n:
    phan_tu = int(input("Nhập phần tử của list: "))
    lst.append(phan_tu)
    i += 1 

binh_phuong = list(map(lambda x: x**2, lst))
print("List chứa bình phương các số hạng là", binh_phuong)
"""

"""
Bài 10:
a) Viết chương trình tạo một list chứa toàn số chẵn thuộc khoảng đóng [1,100].
b) Viết chương trình nhập vào một danh sách các số nguyên từ 1 đến n (n có thể nhập từ bàn phím), sử dụng filter và reduce để viết hàm tính tổng các số chẵn trong danh sách đã nhập.
"""
#Cách 1: Không dùng hàm
lst1_a = []
for i in range(1, 101):
    if i % 2 == 0:
        lst1_a.append(i)
print("List bao gồm các số chẵn là", lst1_a)

n = int(input("Nhập vào một số nguyên: "))
sum_cach_1 = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum_cach_1 += i
print(f"Tổng các số từ 1 đến {n} là {sum_cach_1}")

#Cách 2: Có dùng hàm
def kiem_tra_so_chan(a):
    if a % 2 == 0: 
        return True
lst2_a = []
for i in range(1, 101):
    if kiem_tra_so_chan(i):
        lst2_a.append(i)
print("List bao gồm các số chẵn là", lst2_a)

n = int(input("Nhập vào một số nguyên: "))
sum_cach_2 = 0
for i in range(1, n+1):
    if kiem_tra_so_chan(i):
        sum_cach_2 += i
print(f"Tổng các số từ 1 đến {n} là {sum_cach_2}")

# Cách 3: sử dụng lambda, map, filter, reduce
lst3_a = list(filter(lambda x: x % 2 ==0, range(1, 101)))
print("List bao gồm các số chẵn là", lst3_a)
import functools
n = int(input("Nhập vào một số nguyên: "))
sum_cach_3 = functools.reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 ==0, range(1, n+1))))
print(f"Tổng các số từ 1 đến {n} là {sum_cach_3}")