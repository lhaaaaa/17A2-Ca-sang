"""
Bài 1:
Viết một module sohoc.py trong đó gồm các phương thức tính toán cơ bản: 
cộng, trừ, nhân, chia, lũy thừa. Sau đó viết chương trình tính toán số 
học dựa trên các hàm được viết và lưu trong module sohoc.

import sohoc
a,b = map(float, input("Nhập vào 2 số a, b: ").split())
phep_cong = sohoc.phep_cong(a,b)
phep_tru = sohoc.phep_tru(a,b)
phep_nhan = sohoc.phep_nhan(a,b)
phep_chia = sohoc.phep_chia(a,b)
phep_luy_thua = sohoc.phep_luy_thua(a,b)
print("Phép cộng hai số a, b là:", phep_cong)
print("Phép trừ hai số a, b là:", phep_tru)
print("Phép nhân hai số a, b là:", phep_nhan)
print("Phép chia hai số a, b là:", phep_chia)
print("Phép lũy thừa hai số a, b:", phep_luy_thua)
"""

"""
Giả sử cho một danh sách A = [[1,2,3], [4,5,6], [7,8,9]]. Thực hiện các 
yêu cầu sau:
2.1. Xây dựng một module đặt tên là MyMatrix chứa các phương thức bổ 
sung cho đối tượng danh sách, trong đó viết các hàm dưới đây:
a) isMatrix(A) kiểm tra lại xem list A có phải là một biểu diễn ma trận 
không? Trả về kết quả True nếu đúng và False nếu sai
b) inMatrix(A), hàm in ma trận A ra màn hình
c) isSquare(A), kiểm tra xem A có là ma trận vuông không?
d) ChangeRow(A,i,j), hàm thay đổi 2 hàng của ma trận A. Nếu A không phải 
là ma trận hoặc không thực hiện được thì trả lại False, nếu thực hiện 
thành công thì trả về True.
e) Change Column(A,i,j), hàm thay đổi 2 cột của ma trận A. Nếu A không 
phải là ma trận hoặc không thực hiện được thì trả lại False, nêu thực hiện
thành công thì trả về True.
f) Transpose(A), hàm trả lại kết quả là ma trận A^T là ma trận chuyển vị 
của A.
g) GetSymetry (A), kiêm tra ma trận vuông A có phải là ma trận đối xứng 
không 2 Trả về kết quả là True nếu A là ma trận đối xứng và False nếu A 
không phải là ma trận đối xứng.
2.2. Viết chương trình sử dụng các hàm trong module MyMatrix vừa được xây 
dựng ở trên để kiểm tra danh sách A có thỏa mãn các điều kiện trong mục 2.1.

import MyMatrix
A = [[1,2,3], [4,5,6], [7,8,9]]
#Kiểm tra A có phải là ma trận
if MyMatrix.isMatrix(A):
    print("A là một ma trận")

#In ma trận A
MyMatrix.inMatrix(A)

#Kiểm tra ma trận vuông
if MyMatrix.isSquare(A):
    print("A là ma trận vuông")
else:
    print("A không là ma trận vuông")

#Tráo đổi 2 hàng
trao_doi_hang = MyMatrix.changeRow(A, 0, 2)
print(trao_doi_hang)

#Tráo đổi 2 cột
trao_doi_cot = MyMatrix.changeCol(A, 1, 2)
print(trao_doi_cot)

#In ra ma trận chuyển vị
chuyen_vi = MyMatrix.transpose(A)
print(chuyen_vi)

# Kiểm tra ma trận đối xứng
if MyMatrix.GetSymetry(A):
    print("A là ma trận đối xứng")
else:
    print("A không là ma trận đối xứng")
"""

"""
Bài 3:
Xây dựng một module có tên Tinh_Toán_Matrix.py gồm các phương thức sau:
+ Add Matrix(A,B), hàm trả về tổng của 2 ma trận.
+ Sub Matrix(A.B), hàm trả vệ hiệu của 2 ma trận.
+ Mul Matrix(A,B), hàm trả về tích của 2 ma trận.
Viết chương trình sử dụng module Tình_ Toan Matrix.py.

import tinh_toan_matrix
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
cong_ma_tran = tinh_toan_matrix.cong_ma_tran(A,B)
print("Phép cộng hai ma trận:", cong_ma_tran)

tru_ma_tran = tinh_toan_matrix.tru_ma_tran(A,B)
print("Phép trừ hai ma trận:", tru_ma_tran)

nhan_ma_tran = tinh_toan_matrix.nhan_ma_tran(A,B)
print("Phép nhân hai ma trận:", nhan_ma_tran)
"""

"""
Bài 5:
Xây dựng một package có tên là mypackage gồm có các module MyMatrix.py 
và tinh_toan_Matrix.py đã viết ở bài tập trên. Viết chương trình có sử 
dụng package mypackage.
"""
from mypackage import MyMatrix, tinh_toan_matrix
A = [[1,2,3], [4,5,6], [7,8,9]]
#Kiểm tra A có phải là ma trận
if MyMatrix.isMatrix(A):
    print("A là một ma trận")

#In ma trận A
MyMatrix.inMatrix(A)

#Kiểm tra ma trận vuông
if MyMatrix.isSquare(A):
    print("A là ma trận vuông")
else:
    print("A không là ma trận vuông")

#Tráo đổi 2 hàng
trao_doi_hang = MyMatrix.changeRow(A, 0, 2)
print(trao_doi_hang)

#Tráo đổi 2 cột
trao_doi_cot = MyMatrix.changeCol(A, 1, 2)
print(trao_doi_cot)

#In ra ma trận chuyển vị
chuyen_vi = MyMatrix.transpose(A)
print(chuyen_vi)

# Kiểm tra ma trận đối xứng
if MyMatrix.GetSymetry(A):
    print("A là ma trận đối xứng")
else:
    print("A không là ma trận đối xứng")

C = [[1,2],[3,4]]
B = [[5,6],[7,8]]
cong_ma_tran = tinh_toan_matrix.cong_ma_tran(C,B)
print("Phép cộng hai ma trận:", cong_ma_tran)

tru_ma_tran = tinh_toan_matrix.tru_ma_tran(C,B)
print("Phép trừ hai ma trận:", tru_ma_tran)

nhan_ma_tran = tinh_toan_matrix.nhan_ma_tran(C,B)
print("Phép nhân hai ma trận:", nhan_ma_tran)