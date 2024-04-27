# Khởi tạo list, mảng 
mang_1_chieu = [6, 3.5, "17A2", 6]

# Độ dài của một list
#print(len(mang_1_chieu))

# Truy cập vào từng phần tử bằng cách sử dụng chỉ số
#for i in range(len(mang_1_chieu)): #Truy cập vào từng chỉ số của phần tử trong mảng
#    print(mang_1_chieu[i])

# Truy cập vào từng phần tử trong mảng
#for i in mang_1_chieu: # Truy cập vào từng phần tử trong chuỗi
#    print(i)

# Thao tác cơ bản trên list

# Thêm phần tử vào list:
# Sử dụng append: thêm phần tử vào CUỐI list
#print(mang_1_chieu) # Mảng ban đầu
# mang_1_chieu.append(5)
# print(mang_1_chieu) # Mảng sau khi sử dụng append
# Sử dụng insert: thêm phần tử vào VỊ TRÍ BẤT KÌ trong list
#mang_1_chieu.insert(1, 5)
#print(mang_1_chieu) # Mảng sau khi sử dụng insert

# Xóa phần tử khỏi list
# Sử dụng remove: xóa phần tử xuất hiện lần đầu tiên
# mang_1_chieu.remove(6)
# print(mang_1_chieu)
# Sử dụng pop: xóa phần tử ở index mong muốn, trả về phần tử đó
#print(mang_1_chieu.pop(3))
# Sử dụng del: 
#del mang_1_chieu[2] # xóa phần tử ở index mong muốn ra khỏi list
#del mang_1_chieu # xóa toàn bộ mảng
# Sử dụng clear
#mang_1_chieu.clear()
#print(mang_1_chieu)

# Truy cập vào phần tử trong list
#print(mang_1_chieu[1]) #Truy cập từng phần tử trong list
#print(mang_1_chieu[:3]) #Truy cập các phần tử trong list
#print(mang_1_chieu[:-1]) 

# Thay đổi phần tử trong list
#mang_1_chieu[3] = 7
#print(mang_1_chieu)

# Tìm phần tử lớn nhất trong list
mang = [4, 6, 9, 10, 3, 2]
# Không sử dụng hàm max()
#max = 0
#for i in mang:
#    if max < i:
#        max = i
#print(max)

# Sử dụng hàm max(), min()
#print(max(mang))
#print(min(mang))

# Sắp xếp list
#mang.sort() # Sắp xếp phần tử trong mảng theo chiều tăng dần
#mang.sort(reverse = True) # Sắp xếp phần tử trong mảng theo chiều giảm dần
#print(mang)
#a = sorted(mang) #Trả về một mảng mới đã sắp xếp
#print(mang)
#print(a)

# Kiểm tra sự tồn tại của phần tử
#print(5 in mang) -> Trả về False

# Tạo danh sách mới theo cách thông thường
"""
danh_sach = []
n = 3 
for i in range(3):
    a = input("Nhập vào phần tử: ")
    danh_sach.append(a)
print(danh_sach)
"""

# Tạo danh sách mới bằng list comprehension
#danh_sach = [input("Nhập vào một phần tử thứ {}".format(i+1)) for i in range(3)]
#print(danh_sach)
#danh_sach = [i**2 for i in range(5) if i % 2 == 0]
#print(danh_sach)

# Tạo một ma trận
#matrix = [[1, 2, 3], [4, 5, 6]]
#a = matrix[1][1]
#print(a)