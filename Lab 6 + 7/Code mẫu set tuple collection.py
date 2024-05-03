#--------------------------------------------------
# Lý thuyết về tuple
# Khai báo một tuple
#tuple1 = (1,2,3,4)
#print(tuple1)

# Xác định độ dài của tuple 
#print(len(tuple1))

# Truy cập vào từng phần tử trong tuple
#a = tuple1[2]
#print(a)

# Sử dụng vòng lặp với tuple
# Truy cập theo index trong tuple
#for index in range(len(tuple1)):
#    print(tuple1[index], end = " ")
#print()
# Truy cập theo phần tử trong tuple 
#for element in tuple1:
#    print(element, end = " ")
#print()
# Truy cập theo index và phần tử trong tuple
#for index, element in enumerate(tuple1):
#    print(tuple1[index], end = "")
#    print(element, end = " ")
#   print(index)

# Truy cập các phần tử, chỉ mục trong tuple
# Truy cập vào một phần tử trong tuple
#print(tuple1[1])
# Sử dụng slicing, truy cập vào nhiều phần tử, in ra một tuple con
#print(tuple1[0:2])
#print(tuple1[:2])
#print(tuple1[2:])
#print(tuple1[::-1])
# Sử dụng phương thức index() -> In ra index của phần tử đang xem xét
#print(tuple1.index(2))

# Nối các tuple
#tuple2 = (5,6,7,8)
#tuple3 = tuple1 + tuple2
#print(tuple3)
#tuple4 = tuple1 + (1,) # "thêm phần tử" vào trong tuple
#print(tuple4)

# Đếm số lượng phần tử trong tuple
#print(tuple4.count(1))

# Tìm giá trị lớn nhất và giá trị nhỏ nhất
#print(max(tuple4))
#print(min(tuple4))

# Khai báo một tuple trống và "thêm phần tử" vào tuple đó
#tuple = () 
#while True:
#    a = input("Nhập giá trị một thêm vào tuple: ") 
#    if a == "0":
#        break
#    tuple = tuple + (a,)
#print(tuple)

#-------------------------------------
# Lý thuyết về set
# Khởi tạo set
set1 = {1,2,3,4,5}
#print(set1)
# Độ dài của một set
#print(len(set1))
# Sử dụng vòng lặp với set
#for element in set1:
#    print(element, end = " ")

# Các thao tác cơ bản trên set

# Thêm phần tử vào set
# Sử dụng phương thức add
#set1.add(6)
#print(set1)
# Sử dụng phương thức update
#set1.update({6,7,8})
#print(set1)
# Sử dụng toán tử |=
#set1 |= {7}
#print(set1)

# Xóa phần tử khỏi set: Sử dụng phương thức remove(), discard(), pop(), clear(), del hoặc toán tử -=
# Sử dụng phương thức remove
#set1.remove(5) #-> Xóa và không lưu trữ phần tử đã xóa
#print(set1)
# Sử dụng phương thức pop
#b = set1.pop() -> Rút phần tử và lưu trữ vào biến a
#print(b)
#print(set1)
# Sử dụng phương thức discard
#set1.discard(5)
#print(set1)
# Sử dụng phương thức clear
#set1.clear()
#print(set1)
# Sử dụng del
# Sử dụng toán tử -=
#set1 -= {5}
#print(set1)

# Phép toán hợp các tập hợp
# Sử dụng toán tử |
#set2 = {6,7,8,9,10}
#set3 = {11}
#union_set = set1 | set2 | set3 
#print(union_set)
# Sử dụng phương thức union
#union_set1 = set1.union(set2).union(set3)
#print(union_set1)

# Phép toán giao các tập hợp
#set2 = {4,5,6}
# Sử dụng toán tử &
#set_giao = set1 & set2
#print(set_giao)
# Sử dụng phương thức intersection
#set_giao1 = set1.intersection(set2)
#print(set_giao1)

# Phép toán hiệu 2 tập hợp
# Sử dụng toán tử -
set2 = {4,5,6}
set3 = {7,8,9}
#hieu_set = set2 - set1
#print(hieu_set)
# Sử dụng toán tử difference
#hieu_set1 = set1.difference(set2)
#print(hieu_set1)

# Thay đổi tập hợp dựa trên phép toán tập hợp
#set1.difference_update(set2)
#print(set1)
#a = set1.symmetric_difference(set2)
#print(a)

# Các phương thức khác
#print(set3.isdisjoint(set2)) #Kiểm tra 2 tập hợp có giao nhau không
#print(set1.issubset(set2)) #Kiểm tra tập hợp set2 có là con của set1 không
#print(set1.issuperset(set2)) #Kiểm tra set2 có là cha của set1 không


