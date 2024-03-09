#Bài 1
#Tạo biến tên gọi là retained
#retained = 100
#interest = 0.15
#total = retained * ((1.0+interest)**10)
#print("Số liền nhận được sau 10 năm là {:.2f}".format(total))

#Bài 3
"""
print(
    
Shall I compare thee to a summer's day?
Thou art more lovely and more temperate: 
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date:
    Sometime too hot the eye of heaven shines,
	And often is his gold complexion dimmed;
	And every fair from fair sometime declines,
	By chance or nature's changing course untrimmed;
But thy eternal summer shall not fade
Nor lose possession of that fair thou owest;
Nor shall Death brag thou wanderest in his shade,
When in eternal lines to time thou growest:
	So long as men can breathe or eyes can see,
	So long lives this, and this gives life to thee.
(Sonnet 18 by William Shakespeare)
    
)
"""

#Bài 4
#Bước 1: Nhập nhiệt độ C từ bàn phím
#nhiet_do_c = float(input("Nhập nhiệt độ: "))
#Bước 2: Đổi đơn vị từ độ C sang độ K
#nhiet_do_k = nhiet_do_c + 273.15
#Bước 3: In kết quả ra màn hình
#print("{} độ C chuyển sang độ K là {}".format(nhiet_do_c, nhiet_do_k))

#Bài 5
#Nhập hai số nguyên dương m, n
#m,n = map(int, input("Nhập hai số nguyên dương").split())
#Phần nguyên của phép chia m cho n 
#print("Phần nguyên của phép chia là {}".format(m//n))
#Phần dư của phép chia m cho n
#print("Phần dư của phép chia là {}".format(m%n))

#Bài 6
import math
#Nhập bán kính từ bàn phím
#r = float(input("Nhập bán kính: "))
#Tính và in ra diện tích hình tròn
#s = math.pi *r *r
#print("Diện tích hình tròn là ", s)

#Bài 6
#Nhập độ cao h
#h = float(input("Nhập độ cao: "))
#Tính vận tốc rơi tự do
#g = 9.8 #m/s^2, gia tốc
#v1 = math.sqrt(2*g*h)
#v2 = (2*g*h)**0.5
#print("Vận tốc rơi tự do 1 là {:.2f} m/s".format(v1))
#print("Vận tốc rơi tự do 2 là {:.2f} m/s".format(v2))

#Bài 8
#Nhập độ dài đáy lớn, đáy nhỏ, chiều cao
#a,b,h = map(float, input("Nhập các số đo: ").split())
#Tính diện tích hình thang
#s = (a + b)*h/2
#print("Diện tích hình thang là:", s)

#Bài 9
#Nhập độ dài 3 cạnh tam giác
#a,b,c = map(float, input("Nhập các số đo: ").split())
# Tính và in chu vi diện tích tam giác
#d = a + b + c
#p = d/2
#s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#print("Chu vi tam giác là {} và diện tích tam giác là {}".format(d,s))

#Bài 10
#Nhập x, y từ bàn phím
x, y = map(float, input("Nhập các số x,y: ").split())
#Tính và in kết quả f(x)
tu = math.sin(x)
mau = (2*x + y)/math.cos(x) - x**y/(x-y)
print("Kết quả là:", tu/mau)


