"""
Bài 1:
Viết chương trình nhập nội dung tập hợp hoa quả từ bàn phím và 
lưu vào một tập hợp có tên là hoaqua. Việc nhập liệu kết thúc khi nhập vào 
ký tự "q'.
Thực hiện các yêu cầu:
a) In các loại quả trong tập hợp đã nhập ra màn hình.
b) Kiểm tra xem một loại quả được nhập từ bàn phím có thuộc thuộc tập hợp 
hoaqua không?

# Nhập các loại quả từ bàn phím
hoaqua = set()
while True:
    qua = input("Nhập loại quả từ bàn phím: ")
    if qua == "q":
        break
    hoaqua.add(qua)
print(hoaqua)
# In các loại quả từ tập hợp
for qua in hoaqua:
    print(qua, end = ' ')
# Nhập hoa quả kiểm tra
kiem_tra_qua = input("\n Nhập loại quả muốn kiểm tra: ")
if kiem_tra_qua in hoaqua:
    print("Quả muốn kiểm tra có trong tập hợp")
else:
    print("Quả muốn kiểm tra không nằm trong tập hợp")
"""

"""
Bài 2:
Viết chương trình thực hiện các việc sau đối với Set:
a) Thêm một phần tử.
b) Xóa bỏ một phần tử bằng remove().
c) Xóa bỏ một phần tử bằng discard().
d) Xóa bỏ một phần tử ngẫu nhiên.
e) Thêm nhiều phần tử vào Set.

my_set = set()
# Thêm một phần tử
my_set.add(7)
my_set.add(8)
my_set.add(9)
my_set.add(10)
print(my_set)
# Xóa bỏ một phần tử bằng remove()
my_set.remove(7)
print(my_set)
# Xóa bỏ một phần tử bằng discard
my_set.discard(7)
print(my_set)
# Xóa bỏ một phần tử ngẫu nhiên 
my_set.pop()
print(my_set)
# Thêm nhiều phần tử vào set
my_set.update({1,2,3,4})
print(my_set)
"""

"""
Bài 3:
Cho 2 tập hợp A = {1,2,3,4}; B = {3,4,5,6}. Thực hiện các yêu cầu sau:
a) Viết chương trình kiểm tra tập hợp A có là con của tập hợp B không?
b) Kiểm tra 2 tập hợp có rời nhau không?
c) Viết code thực hiên các phép hợp, giao, hiệu, hiệu đối xứng của A, B

A = {1,2,3,4}
B = {3,4,5,6}
# Kiểm tra tập hợp A có là con của tập hợp B không?
print(A.issubset(B))
# Kiểm tra 2 tập hợp có rời nhau (không có phần tử chung) không?
print(A.isdisjoint(B))
# Hợp 2 tập hợp
C = A.union(B)
print(C)
# Giao 2 tập hợp
D = A.intersection(B)
print(D)
# Hiệu 2 tập hợp
E = A.difference(B)
print(E)
# Hiệu đối xứng 
F = A.symmetric_difference(B)
print(F)
"""

"""
Bài 4:
Cho tập hợp my_ set bao gồm các phần tử chỉ là số hoặc xâu ký tự. 
Chẳng hạn: my_set={1,2, "Táo", 3.14, 'Pi'}.
Viết chương trình tách tập hợp my _set thành hai tập con N 
(chỉ chứa số nguyên hoặc thập phân) và S(chỉ chứa xâu ký tự).

my_set= {1,2, "Táo", 3.14, 'Pi'}
N = set()
S = set()
for element in my_set:
    if type(element) == int or type(element) == float:
        N.add(element)
    elif type(element) == str:
        S.add(element)
print(N)
print(S)
"""

"""
Bài 5:
a) Viết chương trình tạo tập hợp A chỉ bao gồm các số nguyên tố nhỏ hơn n với n được nhập từ bàn phím.
b) Viết chương trình tạo ngẫu nhiên 2 tập hợp số tự nhiên B, C sau đó liệt kê ra màn hình các phần tử chung của A, B.
c) Viết chương trình sinh các tập hợp A, B, C như sau:
D- là tập hợp 100 số tự nhiên ngẫu nhiên trong khoảng [1,1000].
E- là tập hợp 20 số tự nhiên ngẫu nhiên lấy từ tập hợp D.
F- là tập hợp 10 số tự nhiên ngẫu nhiên lấy từ E.
d) Viết chương trình sinh các tập hợp A, B có ý nghĩa như sau:
A- là tập hợp 10 số tự nhiên ngẫu nhiên lấy từ khoảng [2,1000].
B- Tập tất cả các số là ước số nguyên tố của các số lấy từ A. Tức là một số p thuộc B khi và chỉ khi: p là số nguyên tố và p là ước số của một số nằm trong A 
(Ước số có thể bao gồm cả 1 và chính nó). 
"""

n = int(input("Nhập số nguyên: "))
# a) Viết chương trình tạo tập hợp A chỉ bao gồm các số nguyên tố nhỏ hơn n với n được nhập từ bàn phím.
A = set()
for i in range(n):
    if i < 2:
        continue
    else:
        check = True
        for j in range(2,i):
            if i % j == 0:
                check = False
        if check == True:
            A.add(i)
print(A)

#b) Viết chương trình tạo ngẫu nhiên 2 tập hợp số tự nhiên B, C sau đó liệt kê ra màn hình các phần tử chung của B, C.
import random
B = set()
C = set() 
for i in range(n):
    random_interger1 = random.randint(1,10)
    B.add(random_interger1)
    random_interger2 = random.randint(1,10)
    C.add(random_interger2)
print(B)
print(C)
print("Phần tử chung của 2 tập hợp là:", B.intersection(C))

# c) D- là tập hợp 100 số tự nhiên ngẫu nhiên trong khoảng [1,1000]
D = set()
for i in range(100):
    so = random.randint(1,1000)
    D.add(so)
print(D)

# E- là tập hợp 20 số tự nhiên ngẫu nhiên lấy từ tập hợp D
E = set()
for i in range(20):
    so = random.randint(1,1000)
    E.add(so)
print(E)

# F- là tập hợp 10 số tự nhiên ngẫu nhiên lấy từ tập hợp D
F = set()
for i in range(10):
    so = random.randint(1,1000)
    F.add(so)
print(F)

#d) G- là tập hợp 10 số tự nhiên ngẫu nhiên lấy từ khoảng [2,1000]
G = set()
for i in range(10):
    so = random.randint(2,1000)
    G.add(so)
print(G)

H = set()
for element in G:
    check = True
    for i in range(2,element):
        if element % i == 0:
            check = False
    if check == True:
        H.add(element)
print(H)


