# Hàm range()
#range(1,8,2)
"""
Giá trị khởi đầu bằng 1
Giá trị kết thúc bằng 8 - 1 = 7
Bước nhảy: 2 
-> Tạo ra một chuỗi số nguyên: 1, 3, 5, 7
"""
#range(5)
"""
Mặc định:
+ Giá trị khởi đầu bằng 0
+ Bước nhảy: 1
Giá trị kết thúc bằng 5 - 1 = 4 
-> Tạo ra một chuỗi số nguyên: 0, 1, 2, 3, 4
"""
#range(-1, -2)
"""
Giá trị khởi đầu bằng 0
Giá trị kết thúc bằng -2 + 1 = -1
Bước nhảy bằng -1
-> Tạo ra một chuỗi số nguyên giảm dần: 0, -1
"""

# Vòng lặp for
# Biến chạy i không cần khai báo trước
#for i in range(1,4,2):
#    print(i)
"""
Cách thức hoạt động của chương trình:
Bước 1: Khởi tạo vòng lặp for với biến i chạy trong hàm range(1,4,2)
Bước 2: chạy vòng lặp:
i = 1 -> nhảy vào tác vụ bên trong: in ra giá trị i: in ra 1 -> Biến i + bước nhảy: i + 2 = 1 + 2 = 3
i = 3 -> nhảy vào tác vụ bên trong: in ra giá trị i: in ra 3 -> Biến i + 2 = 5 -> Kết thúc vòng lặp
"""
#j = 5
#for i in range(5):
#    print(j)
"""
Cách thức hoạt động của chương trình:
Bước 1: Khởi tạo vòng lặp for với biến i chạy trong hàm range(5)
Bước 2: chạy vòng lặp:
i = 0 -> in ra giá trị j = 5 -> Biến i + 1 = 1
i = 1 -> in ra giá trị j = 5 -> Biến i + 1 = 2
i = 2 
i = 3
i = 4 -> in ra giá trị j = 5 -> dừng chương trình
"""
#for a in range(5):
#    print("Hello")
#print(a)