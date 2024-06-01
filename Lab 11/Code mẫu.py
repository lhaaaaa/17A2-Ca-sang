"""
# Sử dụng open
fruit = open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest.txt", "r")
# In ra tên file
print("Tên của file là", fruit.name)
# Xem chế độ mở file
print("Chế độ mở file", fruit.mode)
# Đóng file
fruit.close()
"""
"""
# Sử dụng câu lệnh with
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest.txt", "r") as fruit:
    print("Tên của file là", fruit.name)
"""

#Đọc dữ liệu từ file
"""
Phương thức read():
+ Đọc toàn bộ file trong một lần
+ Trả về chuỗi dữ liệu
+ Thích hợp khi muốn đọc file trong 1 lần, dữ liệu không quá lớn

fruit = open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest.txt", "r")
content = fruit.read()
print(content)
fruit.close()

Phương thức readline():
+ Đọc và trả về một dòng dữ liệu từ file, bao gồm ký tự newline (\n) ở cuối dòng
+ Thích hợp khi muốn đọc file ở từng dòng
+ Nếu muốn đọc dòng theo ý muốn, sử dụng vòng lặp

fruit = open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest.txt", "r")
#line1 = fruit.readline()
#line2 = fruit.readline()
#line3 = fruit.readline()
#print(line1, line2, line3)
# Đọc dòng mong muốn
for i in range(1):
    fruit.readline() #Bỏ qua 1 dòng đầu
line2_ = fruit.readline()
print(line2_)


Phương thức readlines():
+ Đọc tất cả các dòng dữ liệu và trả về dưới dạng một list
+ Mỗi phần tử trong list ở dạng chuỗi, bao gồm ký tự newline
+ Đọc dòng theo ý muốn, sử dụng chỉ mục trong list

fruit = open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest.txt", "r")
content = fruit.readlines()
print(content)
line1_ = content[0]
print(line1_)
fruit.close()

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest.txt", "r") as fruit2:
    content2 = fruit2.readlines()
    print(content2[1])
"""
# Ghi dữ liệu vào tập tin
"""
Phương thức write():
+ Ghi từng dòng dữ liệu vào tập tin
+ Nếu muốn ghi dữ liệu từ một danh sách cho trước, ta sử dụng vòng lặp

test2 = open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest2.txt", "w")
test2.write("Day la dong dau tien \n")
test2.write("Day la dong so 2")
lst = ["Dong 1", "Dong 2", "Dong 3"]
test3 = open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest3.txt", "w")
for item in lst:
    test3.write(item + "\n")
test3.close()
"""

"""
Phương thức writelines():
+ Ghi một chuỗi các dòng vào trong tập tin
+ Thích hợp sử dụng với việc ghi file từ một danh sách

lst = ["Dong 1 \n", "Dong 2\n", "Dong 3\n"]
test2 = open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/filetest2.txt", "w")
test2.writelines(lst)
"""
# Làm việc với file csv
import csv
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/username.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
data = [["smith79", "5079", "Jamie", "Smith"]]
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-sang/Lab 11/username.csv", "a", newline= "") as file:
    for row in data:
        line = ";".join(row) + '\n'
        file.writelines([line])