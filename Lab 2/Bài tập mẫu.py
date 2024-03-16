# Bài 1
"""
Tính năm nhuận. Năm thứ n là nhuận nếu có: 
Mệnh đề 1[chia hết cho 4 and nhưng không chia hết cho 100] 
hoặc (or) 
Mệnh đề 2[năm đó chia hết cho 400]
"""
#n = int(input("Nhập vào một năm để kiểm tra: "))
#if (n % 4 == 0 and n % 100 != 100) or (n % 400 ==0):
#    print("Năm {} là năm nhuận".format(n))
#else:
#    print("Năm {} không là năm nhuận".format(n))

# Bài 2
"""
Viết chương trình kiểm tra xem điểm M(x, y) có nằm trong hình tròn tâm I(a, b) 
và bán kính R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn 
và False nếu nằm ngoài hình tròn với x, y, a, b, R nhập vào từ bàn phím.
"""

# Bài 3
"""
Viết chương trình nhập vào các số a, b, c sau đó kiểm tra bộ ba số a, b, c 
vừa nhập vào là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, 
tam giác vuông cân, tam giác đều hay không phải là bộ ba cạnh của tam giác.
"""

#a,b,c = map(int, input("Nhập vào số đo của 3 cạnh: ").split())
#a = 1 
#b = 1 
#c = 2 **0.5
#if (a + b > c) and (a + c > b) and (b + c > a): #Kiểm tra điều kiện tam giác
#    if (a == b) and (a == c) and (b == c): #Kiểm tra điều kiện tam giác đều
#        print("Bộ ba số đo lập thành tam giác đều")
#    elif (a == b) or (a == c) or (b == c): # Kiểm tra điều kiện tam giác cân
#        if (int(a ** 2 + b**2) == int(c **2)) or (int(a**2 + c**2) == int(b**2) ) or (int(b **2 + c**2) == int(a**2)): #Kiểm tra điều kiện vuông cân
#            print("Bộ ba số đo lập thành tam giác vuông cân")
#        else:
#            print("Bộ ba số đo lập thành tam giác cân")
#    elif (a ** 2 + b**2 == c **2) or (a**2 + c**2 == b**2 ) or (b **2 + c**2 == a**2): #Kiểm tra điều kiện tam giác vuông
#        print("Bộ ba số đo lập thành tam giác vuông")
#    else:
#        print("Bộ ba số đo lập thành tam giác thường")
#else: 
#    print("Bộ ba số đo không phải là bộ ba cạnh của tam giác")

# Bài 4
"""
Viết chương trình tìm số lớn nhất trong 3 số bằng Python
max = a 
Kiểm tra max có lớn hơn b hay không: max = b 
Kiểm tra số max có lớn hơn c hay không: max = c
In số lớn nhất trong 3 số
"""
# Bài 5
"""
Viết chương trình kiểm tra một ký tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm
Ký tự là bất kỳ được nhập từ bàn phím
Nguyên âm: UE OAI
"""
#ky_tu = input("Nhập vào một ký tự: ")
#if  (ky_tu == 'u') or (ky_tu == 'U') or (ky_tu == 'e') or (ky_tu == 'E') or (ky_tu == 'o') or (ky_tu == 'O') or (ky_tu == 'a') or (ky_tu == 'A') or (ky_tu == 'i') or (ky_tu == 'I'):
#    print("Ký tự đã nhập là nguyên âm")
#else:
#    print("Ký tự đã nhập là phụ âm")

# Bài 7
# Viết chương trình giải hệ phương trình bậc nhất 2 ẩn
#a1, b1, c1 = map(float, input("Nhập các hệ số của phương trình 1: ").split())
#a2, b2, c2 = map(float, input("Nhập các hệ số của phương trình 2: ").split())
#d = a1 * b2 - a2 * b1
#dx = c1 * b2 - c2 * b1
#dy = a1 * c2 - a2 * c1
#if d == 0:
#    if dx == 0 and dy == 0:
#        print("Hệ phương trình có vô số nghiệm")
#    else:
#        print("Hệ phương trình vô nghiệm")
#else:
#    x = dx/d
#    y = dy/d
#    print("Hệ phương trình có nghiệm duy nhất (x,y) = ({},{})".format(x,y))

# Bài 9
"""
Tính cước taxi:
Viết chương trình tính cước taxi theo biểu phí cơ bản như sau:
+ Loại xe 4 chỗ:
Giá mở cửa: 11.000 đồng/0.8km         Trong phạm vi 20km: 12.100 đồng/km     Từ km thứ 21 trở đi: 10.000 đồng/km
+ Loại xe 7 chỗ:
Giá mở cửa: 13.000 đồng/0.8km	Trong phạm vi 30km: 14.000 đồng/km	     Từ km thứ 31 trở đi: 12.000 đồng/km
Tiền chờ: 5 phút đầu được miễn phí, từ phút thứ sáu trở đi là 800 đồng/phút.
Loại xe chỉ nhập 4 hoặc 7.
cước taxi = gia_xe + tien_cho
"""
#loai_xe = int(input("Nhập vào loại xe: "))
#phut_cho = int(input("Nhập số phút chờ: "))
#so_km = float(input("Nhập số km đi được: "))
#tien_cho = 0
#if phut_cho > 5:
#    tien_cho = (phut_cho - 5)*800
#if loai_xe == 4:
#    if so_km < 0.8:
#        gia_xe = 11000
#    elif 0.8 <= so_km < 21:
#        gia_xe = 11000 + (so_km - 0.8)*12100
#    else:
#        gia_xe = 11000 + (21 - 0.8)*12100 + (so_km - 21)*10000
#    cuoc_taxi = gia_xe + tien_cho
#elif loai_xe == 7:
#    if so_km < 0.8:
#        gia_xe = 13000
#    elif 0.8 <= so_km < 31:
#        gia_xe = 13000 + (so_km - 0.8)*14000
#    else:
#        gia_xe = 13000 + (31 - 0.8) *14000 + (so_km - 31) * 12000
#    cuoc_taxi = gia_xe
#else:
#    print("Loại xe không phù hợp")
#print("Tiền cước xe taxi loại {} chỗ là {} đồng".format(loai_xe,cuoc_taxi))

# Bài 10
"""
Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền lương thực sự mà nhân viên đó nhận được).
Với các thông tin giả sử như sau: 
+ 30% thuế thu nhập nếu lương là 15 triệu
+ 20% thuế thu nhập nếu lương từ 7 đến 15 triệu
+ 10% thuế thu nhập nếu lương dưới 7 triệu
"""
luong_nhan_vien = int(input("Nhập tiền lương ban đầu (đơn vị triệu đồng): "))
thue_thu_nhap = 0
if luong_nhan_vien > 15:
    thue_thu_nhap = luong_nhan_vien * 0.3
elif 7 <= luong_nhan_vien <= 15:
    thue_thu_nhap = luong_nhan_vien * 0.2
else:
    thue_thu_nhap = luong_nhan_vien * 0.1
luong_rong = luong_nhan_vien - thue_thu_nhap
print("Tiền lương nhân viên nhận được là: {} triệu đồng".format(luong_rong))