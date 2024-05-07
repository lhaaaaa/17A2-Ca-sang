"""
Bài 1: 
a) Viết chương trình khởi tạo một set với các phần tử là ký tự được 
nhập từ bàn phím. Việc nhập dữ liệu kết thúc khi nhập ký tự "q". 
Xóa các phần tử là ký tự số khỏi tập hợp.
b) Viết chương trình tạo danh sách Numbers các phần tử là số tự nhiên 
nhập từ bàn phím và sinh một tập hợp A với các phần tử thuộc danh sách 
Numbers.
c) Viết chương trình sinh một tập hợp A một cách ngẫu nhiên gồm n số thực 
(n được nhập từ bàn phím). Tìm phần tử nhỏ nhất, 
lớn nhất và tổng các phần tử của tập hợp A.

#A = set()
#while True:
#    ky_tu = input("Nhập một ký tự bất kỳ: ")
#    if ky_tu == "q":
#        break
#    A.add(ky_tu)
#print(A)
#B = set()
#for kytu in A:
#    if kytu not in "0123456789":
#        B.add(kytu)
#print(B)

#numbers = []
#while True:
#    n = int(input("Nhập vào một số tự nhiên: "))
#    if n < 0:
#        break
#    numbers.append(n)
#print(numbers)
#C = set()
#for number in numbers:
#    C.add(number)
#print(C)

import random
A = set()
n = int(input("Nhập một số từ bàn phím: "))
for i in range(n):
    a = random.randint(1,100)
    A.add(a)
print(A)
print("Phần tử lớn nhất trong tập hợp A là:", max(A))
print("Phần tử bé nhất trong tập hợp A là:", min(A))
sum = 0
for so in A:
    sum += so
print("Tổng các phần tử của tập hợp A là:", sum)
"""

"""
Bài 4: 
a) Viết chương trình sinh ngẫu nhiên 2 tập hợp A, B là các ký tự chữ và 
số được nhập từ bàn phím sau đó liệt kê ra màn hình các phần tử chung của A, B.
b) Viết chương tình sinh tập hợp A bao gồm cả số nguyên, số thực và chuỗi ký 
tự. Hãy đếm số phần tử là số nguyên, số thực và chuỗi ký tự của tập hợp A.
c) Viết chương trình thực hiện các công việc sau:
+ Nhập một số tự nhiên n từ bàn phím
+ Tạo 2 tập hợp A, B, trong đó A là tập các số nguyên tố là ước của n; 
Tập hợp B bao gồm các số nguyên tố nhỏ hơn n và không là ước của n.

#A = set()
#while True:
#    ky_tu_A = input("Nhập một ký tự từ bàn phím: ")
#    if ky_tu_A == "q":
#        break
#    A.add(ky_tu_A)
#print(A)
#B = set()
#while True:
#   ky_tu_B = input("Nhập một ký tự từ bàn phím: ")
#    if ky_tu_B == "q":
#        break
#    B.add(ky_tu_B)
#print(B)
#C = A.intersection(B)
#print(C)

#A = ("a", "b", "c", 1, 2, 3, 0.5, 3.5, 2.2, 8.1)
#count1 = 0
#count2 = 0
#count3 = 0
#for phan_tu in A:
#    if type(phan_tu) == int:
#        count1 += 1
#    elif type(phan_tu) == float:
#        count2 += 1
#    elif type(phan_tu) == str:
#        count3 +=1
#print("Số phần tử là số nguyên là:", count1)
#print("Số phần tử là số thực là:", count2)
#print("Số phần tử là chuỗi là:", count3)

n = int(input("Nhập một số tự nhiên từ bàn phím: "))
A = set()
B = set()
uoc = []
for i in range(1,n+1):
    if n % i == 0:
        uoc.append(i)
for so in uoc:
    check = True
    if so < 2:
        continue
    else:
        for j in range(2,so):
            if so % j == 0:
                check = False
        if check == True:
            A.add(so)
print(A)
for i in range(1,n):
    if i in uoc:
        continue
    else:
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
        if check == True:
            B.add(i)
print(B)
"""