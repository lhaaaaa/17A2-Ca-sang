"""
# Hàm không có tham số
# Định nghĩa hàm
def cau_lenh_bat_ky():
    print("Xin chào")
# Chương trình chính
cau_lenh_bat_ky()

# Hàm có tham số
# Định nghĩa hàm
def tong_2_so(so1, so2):
    tong = so1 + so2
    print("Tổng hai số là", tong)
# Chương trình chính
so1 = 3
so2 = 4
tong_2_so(so1, so2)
"""
"""
# Biến cục bộ
def tong_hai_so1(so1, so2):
    tong = so1 + so2
    print("Tổng hai số", tong)

so1 = 3
so2 = 4 
tong_hai_so1(so1, so2)
tong_moi = tong + 4
print(tong_moi) #-> Biến cục bộ, lỗi chương trình

# Biến toàn cục

def tong_hai_so2(so1, so2):
    global tong 
    tong = so1 + so2
    print("Tổng hai số", tong)
tong_hai_so2(so1, so2)
tong_moi = tong + 4
print(tong_moi)
"""

# Tham số bắt buộc
#def tong_hai_so1(so1, so2):
#    tong = so1 + so2
#    print(tong)

#so1 = 3 
#so2 = 4 
#tong_hai_so1(so1, so2)

# Tham số mặc định
#def tong_hai_so2(so1 = 10, so2 = 8):
#    tong = so1 + so2
#    print(tong)
#tong_hai_so2()

# Tham số theo tên, theo từ khóa
#def xin_chao(ten, lop):
#    print("Tên tôi là", ten, "học lớp", lop)

#xin_chao(lop = "17A2", ten = "Nam")

# Tham số có chiều dài thay đổi không xác định 
#def tong_cac_so(*args):
#    for so in args:
#        print(so)
#tup = (1,2,3)
#tong_cac_so(tup)

#def in_thong_tin(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")
#in_thong_tin(name = "Nam", age = 23)

# Hàm lambda
square = lambda x: x**2
print(square(5))

# Hàm filter
numbers = [1,2,3,4,5,6,7,8,9,10]
so_chan = list(filter(lambda x: x % 2 ==0, numbers))
print(so_chan)

# Hàm reduce
import functools
total = functools.reduce(lambda x,y: x + y, numbers) 
print(total)