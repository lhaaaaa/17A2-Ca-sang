"""
Bài 1:
Viết chương trình nhập dữ liệu từ tập tin text file f_in.txt 
và lưu vào một danh sách, in nội dung của danh sách đó ra màn hình.
Biết file text có dạng như sau:
+ Dòng đầu tiên là số tự nhiên n.
+ Dòng thứ hai là n số được viết cách nhau bởi dấu cách.

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/f_in.txt", "r") as bai1:
    n = bai1.readline()
    lstso = bai1.readline()
danhsach = []
danhsachso = []
for so in lstso:
    danhsachso.append(so)
for i in range(2):
    danhsach.append(n)
    danhsach.append(danhsachso)
print(danhsach)
"""

"""
Bài 2:
Viết chương trình xây dựng các hàm thực hiện công việc sau:
+ Đọc dữ liệu từ tập tin dạng text fin.dat và chuyển dữ liệu vào tập tin văn bản fount.dat.
+ Biết rằng tập tin fin.dat có dạng:
- Dòng đầu tiên là một số tự nhiên n.
- n dòng tiếp theo, mỗi dòng là một dãy các số nguyên hoặc thực, cách nhau bởi dấu cách. Số lượng các phần tử của mỗi dãy có thể không bằng nhau.
+ Tệp fout.dat có cấu trúc như sau:
- Dòng đầu tiên ghi số S là tổng của tất cả các số trong dãy từ tệp fin.dat.
- n dòng tiếp theo, dòng thứ i ghi số Si là tổng các số của dãy số tương ứng từ tệp fin.dat.

def docdulieu():
    with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/fin.dat.txt", "r") as file:
        n = file.readline()
        n = int(n)
        tong = []
        for i in range(1,n+1):
            lines = file.readline()
            #Chuyển đổi chuỗi thành danh sách số nguyên 
            data = []
            for num_str in lines.split():
                num = int(num_str)
                data.append(num)
            sum = 0
            for num in data:
                sum += num
            tong.append(sum)
    with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/fount.dat", "w") as file2:
        for item in tong:
            file2.write(str(item)+"\n")

docdulieu()
"""

"""
Bài 5:
Cho trước ma trận A dạng mxn (m hàng, n cột) được mô tả theo danh sách như sau:
A=|[a11, a12,..,a1n], [a21, a22,…,a2n],…,[am1,am2,...,2mn]].
Viết chương trình ghi dữ liệu ma trận A ra tập tin văn bản có dạng sau:
+ Dòng đầu tiên ghi 2 số m, n cách nhau bởi dấu cách
+ m dòng tiếp theo, mỗi hàng ghi dãy các số của hàng tương ứng của ma trận A, các số cách nhau bởi dấu phẩy

m, n = map(int, input("Nhập số hàng và số cột của ma trận A: ").split())
A = []
for i in range(m):
    hang = []
    for j in range(n):
        phantu = int(input(f"Nhập hàng {i+1}, cột {j+1}: "))
        cot = hang.append(phantu)
    A.append(hang)
print(A)

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/matran.txt", "w") as file:
    file.write(str(m) +" "+ str(n) + "\n")
    for i in range(m):
        for j in range(n):
            file.write(str(A[i][j]) + " ")
        file.write("\n")
"""

"""
Bài 6:
Thực hiện ngược lại bài tập 5. Viết chương trình đọc dữ liệu từ tệp 
văn bản trên vào chuyển vào dãy lits A có dạng:
A = [[a11, a12,...,a1n], [a21, a22, ..,a2n],...,[am1,am2,..,2mn]].

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/matran.txt", "r") as file:
    lines = file.readlines()
    m, n = map(int, lines[0].strip().split())
    A = []
    for line in lines[1:]:
        row = [int(x) for x in line.strip().split()]
        A.append(row)

print(f"Ma trận {m} hàng {n} cột là:")
print(A)
"""

"""
Bài 8: 
Giả sử thông tin sinh viên của một lớp gồm các trường sau:  Mã sinh viên, Tên sinh viên, Giới tính, Năm sinh. 
Viết chương trình lưu thông tin sinh viên vào một file .CSV có tên là sinhvien.csv.

sinhvien = []
n = int(input("Nhập số sinh viên: "))
for i in range(1, n+1):
    dict = {}
    dict["Mã sinh viên"] = input(f"Nhập mã sinh viên thứ {i}: ")
    dict["Tên sinh viên"] = input(f"Nhập tên sinh viên thứ {i}: ")
    dict["Giới tính"] = input(f"Nhập giới tính sinh viên thứ {i}: ")
    dict["Năm sinh"] = input(f"Nhập năm sinh sinh viên thứ {i}: ")
    sinhvien.append(dict)
print(sinhvien)
import csv
# Ghi dữ liệu vào file csv
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/sinhvien.csv", "w", newline="", encoding="utf-8") as file:
    fiedname = ["Mã sinh viên", "Tên sinh viên", "Giới tính", "Năm sinh"]
    writer = csv.DictWriter(file, fieldnames= fiedname)
    writer.writeheader()
    for student in sinhvien:
        writer.writerow(student)
"""

"""
Bài 9: 
Giả sử có file sinhvien.csv với nội dung như ở bài trên. Viết chương trình thực hiện các yêu cầu sau:
a) Đọc thông tin sinh viên từ file sinhvien.csv, in dữ liệu các sinh viên ra màn hình.
b) Sắp xếp sinh viên theo thứ tự giảm dần của năm sinh. In ra kết quả trước và sau khi sắp xếp.
c) Thêm một sinh viên mới với đây đủ thông tin được nhập từ bàn phím mà không làm ảnh hưởng kết quả sắp xếp.
d) Tìm kiếm sinh viên có mã số x, với x được nhập từ bàn phím.
e) Xóa sinh viên có năm sinh là y, với y được nhập từ bàn phím
"""
import csv
# Đọc dữ liệu từ file csv
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/sinhvien.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)
# In dữ liệu sinh viên
for student in data:
    print(f"Mã sinh viên: {student["Mã sinh viên"]}")
    print(f"Tên sinh viên: {student["Tên sinh viên"]}")
    print((f"Giới tính: {student["Giới tính"]}"))
    print((f"Năm sinh: {student["Năm sinh"]}"))
    print("----------------")
#Sắp xếp sinh viên theo thứ tự giảm dần của năm sinh. In ra kết quả trước và sau khi sắp xếp.
data.sort(key = lambda x: int(x["Năm sinh"]))
print("Dữ liệu sau khi sắp xếp: ")
# In lại dữ liệu sau khi sắp xếp 
for student in data:
    print(f"Mã sinh viên: {student["Mã sinh viên"]}")
    print(f"Tên sinh viên: {student["Tên sinh viên"]}")
    print((f"Giới tính: {student["Giới tính"]}"))
    print((f"Năm sinh: {student["Năm sinh"]}"))
    print("----------------")
# Thêm thông tin sinh viên từ bàn phím
dict = {}
dict["Mã sinh viên"] = input("Nhập mã sinh viên: ")
dict["Tên sinh viên"] = input("Nhập tên sinh viên thứ: ")
dict["Giới tính"] = input("Nhập giới tính sinh viên thứ: ")
dict["Năm sinh"] = input("Nhập năm sinh sinh viên thứ: ")
data.append(dict)
print(data)

# Tìm kiếm sinh viên có mã số x, với x được nhập từ bàn phím
maso = input("Nhập mã sinh viên cần tìm kiếm: ")
for student in data:
    if student["Mã sinh viên"] == maso:
        print(f"Mã sinh viên: {student["Mã sinh viên"]}")
        print(f"Tên sinh viên: {student["Tên sinh viên"]}")
        print((f"Giới tính: {student["Giới tính"]}"))
        print((f"Năm sinh: {student["Năm sinh"]}"))
        break
    else:
        print("Không có sinh viên cần tìm")

# Xóa sinh viên có năm sinh là y, với y được nhập từ bàn phím
namsinh = input("Nhập năm sinh của sinh viên cần xóa dữ liệu: ")
for student in data:
    if student["Năm sinh"] == namsinh:
        data.remove(student)
        break
    else:
        print("Không có sinh viên cần tìm")
