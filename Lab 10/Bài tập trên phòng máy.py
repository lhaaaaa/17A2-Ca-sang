"""
Bài 1: 
Viết một module my_Triange, chứa các hàm và thủ tục liên quan đến tam giác như sau:
+ is_ TamGiac(a,b,c), hàm kiểm tra xem bộ 3 số a, b, c có tạo thành một 
tam giác không? Trả lại True nếu đúng và False nếu sai.
+ ChuviTamGiac(a,b,c), hàm tính chu vi tam giác
+ S_ TamGiac (a,b,c), hàm tính diện tích tam giác.
Viết chương trình sử dụng module trên.

import my_triange
a,b,c = map(float, input("Nhập vào độ dài a, b, c: ").split())
if my_triange.is_tamgiac(a,b,c):
    print("a,b,c tạo thành 3 cạnh của tam giác")
else: 
    print("a,b,c không tạo thành 3 cạnh của tam giác")

chu_vi = my_triange.chu_vi_tam_giac(a,b,c)
print(chu_vi)

dien_tich = my_triange.dien_tich_tam_giac(a,b,c)
print(dien_tich)
"""

"""
Bài 2: 
Viết môt model my_square, chứa các hàm và thủ tục liên quan 
đến hình vuông như sau.
+ ChuviHinhvuong(a), hàm tính chu vi hình vuông. 
+ Dien_tich_hinh_ vuong (a), hàm tính diện tích hình vuông.
Viết chương trình sử dụng module my _square.

from hinhhoc import my_square
a = float(input("Nhập độ dài cạnh của hình vuông: "))
chu_vi = my_square.chu_vi_hinh_vuong(a)
print("Chu vi hình vuông là:", chu_vi)
dien_tich = my_square.dien_tich_hinh_vuong(a)
print("Diện tích hình vuông là:", dien_tich)

#Bài 10
"""

"""
Bài 3: 
Xây dựng một module có tên sohoc2.py gồm các phương thức:
+ Ucln(a,b), trả về ước chung lớn nhất của 2 số nguyên a, b.
+ Bcnn(a,b), trả về bội số chung nhỏ nhất của 2 số nguyên a, b.
+ SumDivisor(n), trả về tổng các ước của n.
Viết chương trình sử dụng module sohoc2.py trên.

import sohoc2
a,b = map(int, input("Nhập vào 2 số a và b: ").split())
print("Ước chung lớn nhất của 2 số là:", sohoc2.ucln(a,b))
print("Bội chung nhỏ nhất của 2 số là:", sohoc2.bcnn(a,b))
print("Tổng các ước của a là:", sohoc2.tong_uoc(a))
"""

"""
Bài 4: 
Xây dựng module thực hiện các việc sau:
+ Giải phương trình bậc nhất một ẩn.
+ Giải phương trình bậc hai.
Viết chương trình sử dụng module được xây dựng ở trên.


import giaiphuongtrinh
a,b = map(int, input("Nhập hệ số a, b của phương trình bậc nhất: ").split())
nghiem_1 = giaiphuongtrinh.bac_nhat(a,b)
print("Nghiệm của phương trình là:", nghiem_1)

c,d,e = map(int, input("Nhập hệ số c, d, e của phương trình bậc 2: ").split())
nghiem_2, nghiem_3 = giaiphuongtrinh.bac_hai(c,d,e)
if nghiem_2 == nghiem_3:
    print("Phương trình có nghiệm kép:", nghiem_2)
else:
    print("Phương trình có hai nghiệm:", nghiem_2, ",", nghiem_3)
"""

"""
Bài 9: 
Đề quản lý hàng hóa trong một siêu thị với thông tin của mỗi mặt hàng 
bao gồm:mã hàng (là chuỗi 4 ký tự); tênhàng; đơn vị tính; đơn giá; 
số lượng; thành tiền; thuế VAT.
Trong đó: mã hàng; tên hàng; đơn vị tính, đơn giá, số lượng, được nhập 
vào từ bàn phim. 
Xây dựng module qlyhanghoa.py có các chức năng cụ thể sau:
a) Nhập thông tin các mặt hàng từ bàn phím.
b) Tính cột thành tiền với thành tiền = đơn giá* số lượng.
c) Tính cột Thuế với Thuế = thành tiền * 10%.
Viết chương trình sử dụng module qlyhanghoa.py trên.

import qlyhanghoa
#Nhập và lấy thông tin
ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong = qlyhanghoa.nhapthongtin()
#In thông tin
print("Mã hàng:", ma_hang)
print("Tên mặt hàng:", ten_hang)
print("Đơn vị tính", don_vi_tinh)
print("Đơn giá:", don_gia)
print("Số lượng:", so_luong)
#thành tiền
thanh_tien = qlyhanghoa.thanhtien(don_gia, so_luong)
print("Số tiền của mặt hàng là:",thanh_tien)
#thuế
tien_thue = qlyhanghoa.thue(thanh_tien)
print("Tiền thuế là:", tien_thue)
"""

"""
Bài 7: 
Xây dựng một module thực hiện công việc sau:
+ Sinh ngẫu nhiên một dãy số <=100 số nguyên, hiển thị dãy số đó ra màn hình.
+ Liệt kê và hiển thị các số nguyên tố chia hết cho 7 trong dãy đó.
+ Tính tổng các số lẻ thuộc dãy đó.
+ Kiểm tra trong dãy có các số chính phương không? Nếu có hiển thị ra màn hình, ngược lại, in ra thông báo không có số chính phương trong dãy.
Viết chương trình sử dụng module trên.
"""
import bai7
lst_ngau_nhien = bai7.sinh_ngau_nhien()
print(lst_ngau_nhien)

lst_chia_het_7 = bai7.chia_het_7(lst_ngau_nhien)
print(lst_chia_het_7)

lstchinhphuong = bai7.lst_chinh_phuong(lst_ngau_nhien)
print(lstchinhphuong)