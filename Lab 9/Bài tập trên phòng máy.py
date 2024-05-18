"""
Bài 1: 
Viết chương tình nhập 3 số từ bàn phím. 
Sử dụng hàm đệ quy tìm số lớn nhất trong ba số.

def find_max(a,b,c):
    if a >=b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def de_quy_max(a,b,c):
    max_num = find_max(a,b,c)
    if a == max_num or b == max_num or c == max_num:
        return max_num
    else:
        return max(find_max(a,b,max_num), find_max(a,c,max_num), find_max(b,c,max_num))
    
a,b,c = map(int, input("Nhập 3 số nguyên từ bàn phím: ").split())
print("Số lớn nhất trong 3 số là:", de_quy_max(a,b,c))
"""

"""
Bài 2: 
Sử dụng kỹ thuật đệ qui để viết chương trình nhập n số từ bản phím. 
Tính ước chung lớn nhất của n số đó.

def ucln_2_so(a,b):
    if b == 0:
        return a 
    else:
        return ucln_2_so(b, a % b)
    

def ucln_nhieu_so(list_num):
    if len(list_num) == 1:
        return(list_num[0])
    else:
        return ucln_2_so(list_num[0], ucln_nhieu_so(list_num[1:]))
    
numbers = [12, 36, 20]
ket_qua = ucln_nhieu_so(numbers)
print("Ước chung lớn nhất là:", ket_qua)
"""
 
"""
Bài 3: 
Viết chương trình nhập số a, n từ bàn phím. 
Sử dụng hàm đệ qui tính lũy thừa a^n.

def luy_thua(a,n):
    if n == 0:
        return 1
    else:
        return a * (luy_thua(a, n-1))

ket_qua = luy_thua(2,3)
print(ket_qua)
"""

"""
Bài 4: 
Nhập vào từ bàn phim một số tự nhiên, 
in ra tất cả các hoán vị của dãy (1,2,... ).

def hoan_vi(list_num):
    if len(list_num) == 1:
        return [list_num]
    list_hoan_vi = []
    for i in range(len(list_num)):
        current_num = list_num[i]
        list_con_lai = list_num[:i]+list_num[i+1:]
        for j in hoan_vi(list_con_lai):
            list_hoan_vi.append([current_num]+j )
    return list_hoan_vi[-1]

vi_du = [1,2,3]
ket_qua = hoan_vi(vi_du)
print(ket_qua)
"""

"""
Bài 7: 
Viết các hàm tính toán sử dụng kỹ thuật đệ qui, tính tổng

# Tổng 1
def tong1(n):
    if n == 0:
        return 0
    else:
        return 1/(n*(n+1)) + tong1(n-1)
ket_qua1 = tong1(2)
print(ket_qua1)

# Tổng 2
def giai_thua(n):
    if n == 0:
        return 1
    else: 
        return n*giai_thua(n-1)
    
def tong2(n):
    if n == 0:
        return 0
    else:
        return 1/giai_thua(n) + tong2(n-1)
ket_qua2 = tong2(3)
print(ket_qua2)

# Tổng 3
def tong3(n):
    if n == 1:
        return 1
    else:
        return (3*n)**0.5 + tong3(n-1)
ket_qua3 = tong3(3)
print(ket_qua3)
"""

"""
Bài 9:
Tính giai thừa kép:
Biết rằng: Giai thừa kép ký hiệu là n!! được định nghĩa như sau:
n!! = 1, quy ước nếu n = 0 hoặc n = 1
(n - 2)!!n, quy ước nếu n >=2
Tính n!! Sau đó dùng hàm này để tính tổng
S = 1!! - 2!! + …. + (-1)^(k+1)k!! Với k < 1000

def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*giai_thua_kep(n-2)
    
ket_qua = giai_thua_kep(4)
print(ket_qua)
"""

"""
Bài 10:
Có bài toán cổ như sau:
"Vừa gà vừa chó
Bó lại cho tròn
Ba mươi sáu con
Một trăm chân chẵn"
Hỏi có bao nhiêu con gà và bao nhiêu con chó?
Hãy viết chương trình dùng kỹ thuật đệ qui giải bài toán trên?
"""

