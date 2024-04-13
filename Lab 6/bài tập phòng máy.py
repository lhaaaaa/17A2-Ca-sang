"""
Bài 1: 
Cho danh sách a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n = 10 phần tử.
Yêu cầu:
+ Viết chương trình Python tính tổng các phần tử của danh sách.
+ Viết chương trình Python đếm số lượng các số hạng dương và tổng của các số hạng dương.
+ Tìm vị trí của phần tử âm đầu tiên trong danh sách.
+ Tìm vị trí của phần tử dương cuối cùng trong danh sách.
+ Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất.

danh_sach = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# Tính tổng các phần tử của danh sách
sum1 = 0
for i in danh_sach:
    sum1 += i
print("Tổng các phần tử trong danh sách là:", sum1)

# Đếm số lượng các số hạng dương và tổng của các số hạng dương.
sum2 = 0
count = 0
for i in danh_sach:
    if i > 0:
        sum2 += i
        count += 1
print("Tổng các số hạng dương là:", sum2)
print("Số lượng các số hạng dương trong danh sách là:", count)

# Tìm vị trí của phần tử âm đầu tiên trong danh sách
for i in range(len(danh_sach)):
    if danh_sach[i] < 0:
        print("Vị trí của phần tử âm đầu tiên trong danh sách là:", i+1)
        break

# Tìm vị trí của phần tử dương cuối cùng trong danh sách
for i in range(len(danh_sach)-1, -1, -1):
    if danh_sach[i] > 0:
        print("Vị trí của phần tử dương cuối cùng trong danh sách là:", i+1)
        break

# Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất
max = 0
vi_tri = 0
for i in range(len(danh_sach)):
    if max < danh_sach[i]:
        max = danh_sach[i]
        vi_tri = i + 1
print(f"Phần tử lớn nhất trong danh sách là {max} ở vị trí thứ {vi_tri}")
"""

"""
Bài 2: 
Viết chương trình nhập vào một danh sách các phần tử là số nguyên với số phần tử bằng n 
(n nhập từ bàn phím). Thực hiện các yêu cầu sau.
+ Tìm phần tử lớn thứ hai của danh sách và in ra vị trí của phần tử đó.
+ Tính số lượng các số dương liên tiếp nhiều nhất.
+ Tính số lượng các số dương liên tiếp có tổng lớn nhất.

n = int(input("Nhập số lượng phần tử trong danh sách: "))
danh_sach = [int(input("Nhập phần tử thứ {}: ".format(i+1))) for i in range(n)]
print(danh_sach)
max = max(danh_sach)

#Tìm phần tử lớn thứ hai của danh sách và in ra vị trí của phần tử đó
danh_sach_copy = danh_sach.copy()
danh_sach_copy.remove(max)
max2 = 0
vi_tri = 0
for i in range(len(danh_sach_copy)):
    if max2 < danh_sach_copy[i]:
        max2 = danh_sach_copy[i]
        vi_tri += 1
print(f"Phần tử lớn thứ hai trong danh sách là {max2} ở vị trí {vi_tri}")

# Tính số lượng các số dương liên tiếp nhiều nhất
count = 0
for i in range(len(danh_sach)):
    if danh_sach[i] > 0:
        count += 1
    elif danh_sach[i] < 0:
        if danh_sach[i] == danh_sach[-1]:
            break
        count = 0 
print("Số lượng các số dương liên tiếp nhiều nhất là:", count)

# Tính số lượng các số dương liên tiếp có tổng lớn nhất
max_sum = 0 #Tổng lớn nhất
current_sum = 0 #Tổng hiện tại
count1 = 0 
for i in danh_sach:
    if i > 0:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
            count1 = 1 
        elif current_sum == max_sum:
            count1 += 1
        else:
            current_sum = 0 
print("Số lượng các số dương liên tiếp có tổng lớn nhất là: ", count1)
"""

"""
Bài 8: 
Viết chương trình sử dụng lệnh assert để xác minh rằng tất cả các số trong một list được nhập vào là chẵn.

danh_sach1 = [0, 2, 4, 6, 8]
danh_sach2 = [0, 1, 4, 6, 8]
for a in danh_sach1:
    assert a % 2 == 0, "Phần tử trong list không phải là số chẵn"
print("Tất cả các phần tử trong list a là chẵn")
for b in danh_sach2:
    assert b % 2 == 0, "Phần tử trong list không phải là số chẵn"
"""

"""
Bài 16:
2. Ma trận mxn (m hàng, n cột) có thể được mô tả bởi danh sách như sau:
A=|[all, al2, ...aln], [a21, a22,...,a2n], ...,[am1, am2, ..., amn]].
Thực hiện các công việc sau:
a) Viết chương trình nhập vào ma trận A với các phần tử aij là các số tự nhiên được nhập từ bàn phím.
b) Tính tổng các phần tử của Ma trận A.
"""
matrixA = []
m = int(input("Nhập vào số hàng: "))
n = int(input("Nhập vào số cột: "))
for i in range(m):
    row = []
    for j in range(n):
        phan_tu = int(input(f"Nhập giá trị phần tử thứ [{i},{j}]: "))
        row.append(phan_tu)
    matrixA.append(row)
print(matrixA)

sum = 0 
for i in range(len(matrixA)):
    for j in range(len(matrixA[i])):
        sum += matrixA[i][j]
print("Tổng các phần tử trong ma trận A là:", sum)