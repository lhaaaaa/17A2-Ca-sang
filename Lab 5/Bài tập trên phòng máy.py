"""
Bài 1: Nhập từ bàn phím một chuỗi ký tự Str. 
Hãy đếm số các ký tự là số (isnumeric) trong chuỗi ký tự Str và in kết quả ra màn hình.

chuoi = input("Nhập vào một chuỗi: ")
count1 = 0
# Sử dụng vòng lặp xét từng ký tự
for i in chuoi:
    if i.isnumeric():
        count1 += 1
print("Số lượng ký tự là số trong chuỗi trên là:", count1)
# Sử dụng vòng lặp xét từng chỉ mục
count2 = 0
for j in range(len(chuoi)):
    if chuoi[j].isnumeric():
        count2 +=1
print("Số lượng ký tự là số trong chuỗi là:", count2)
"""

"""
Bài 2: Cho trước (hoặc nhập vào từ bàn phím) chuỗi ký tự Str, 
có bao nhiêu ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi ký tự Str.

chuoi = input("Nhập vào một chuỗi: ")
count = 0 
for i in chuoi:
    if i.isnumeric():
        count -= 1 
    else:
        for a in range(65,91):
            if i == chr(a):
                count -= 1 
        for b in range(97, 123):
            if i == chr(b):
                count -= 1
    count += 1
print("Số ký tự không phải chữ cái tiếng Anh và số là:", count)
"""

"""
Bài 3:
Nhập vào một số tự nhiên n từ bàn phím. 
Viết chương trình chuyển số n từ hệ cơ số 10 sang hệ nhị phân. Kết quả là chuỗi nhị phân.

chuoi = ""
n = int(input("Nhập vào số nguyên: "))
if n < 0:
    print("Nhập lại số khác")
else:
    while n > 0:
        phan_du = n % 2
        chuoi = str(phan_du) + chuoi
        n = n // 2
    print("Chuyển số từ hệ 10 sang hệ nhị phân được:", chuoi)
"""

"""
Bài 4:
Cho trước 2 chuỗi ký tự Str1, Str2 (nhập vào từ bàn phím). 
Viết chương trình trộn chuỗi ký tự 1 và 2. Việc trộn Str1 và Str2 thực hiện theo quy tắc sau:
+ Lần lượt từ trái sang phải, viết các ký tự của Str1, sau đó đến Str2
+ Nếu một trong hai chuỗi kết thúc thì chỉ viết ra các ký tự của chuỗi còn lại
Input:
Str1 = “abc”
Str2 = “ghi”
Output: “agbhci”

str1 = input("Nhập vào chuỗi thứ nhất: ")
str2 = input("Nhập vào chuỗi thứ hai: ")
chuoi_gop = ""
min_length = 0
if len(str1) < len(str2):
    min_length = len(str1)
else:
    min_length = len(str2)
for i in range(min_length):
    chuoi_gop += str1[i] + str2[i]

#Xử lý phần còn lại của chuỗi dài hơn
if len(str1) < len(str2):
    chuoi_gop += str2[min_length:]
else:
    chuoi_gop += str1[min_length:]

print("Chuỗi trộn của hai chuỗi đã nhập là:", chuoi_gop)
"""

"""
Bài 5: 
Cho trước (hoặc nhập vào từ bàn phím) chuỗi ký tự Str. 
Hãy xóa đi tất cả các ký tự Str không phải là số, chuỗi ký tự còn lại sẽ là số. 
In ra kết quả chuỗi số này và thông báo cho biết chuỗi đó có phải là số hoàn hảo không.

str1 = input("Nhập một chuỗi từ bàn phím: ")
str2 = ""
for i in str1:
    if i.isnumeric():
        str2 += i
print("Chuỗi chỉ gồm số sau khi tách từ chuỗi ban đầu là:", str2)
# Chuyển kiểu dữ liệu từ chuỗi sang số
so_str2 = int(str2)
sum = 0
for i in range(1,so_str2):
    if so_str2 % i == 0:
        sum += i 
if sum == so_str2:
    print("Chuỗi số đã tách là số hoàn hảo")
"""

"""
Bài 7: 
Cho trước xâu Str là một đoạn văn bản hoàn chỉnh (có thể bao gồm nhiều dòng). 
Nhập vào một từ đơn, hãy tìm trong chuỗi ký tự Str xem chứa bao nhiêu từ đơn này

Hướng dẫn:
Sử dụng count("từ đơn muốn đếm")
"""

"""
Bài 9:
Cho trước hoặc nhập từ bàn phím 2 chuỗi ký tự Str1 và Str2. 
Hãy viết chương trình tìm ra chuỗi ký tự con chung của 2 chuỗi ký tự Str1, Str2 
có độ dài cực đại.
Str1 = "abcdef"
Str2 = "aabbc"
Output:
chuoi = "aabbc"

str1 = input("Nhập vào chuỗi thứ nhất: ")
str2 = input("Nhập vào chuỗi thứ hai: ")
max_chuoi = ""
chuoi_con = ""
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            #Xây dựng chuỗi con
            k = 0
            while (i + k) < len(str1) and (j + k) < len(str2) and str1[i+k] == str2[j + k]:
                chuoi_con += str1[i + k]
                k += 1 
            # Kiểm tra độ dài chuỗi con
            if len(chuoi_con) > len(max_chuoi):
                max_chuoi = chuoi_con
            # Reset chuỗi con
            chuoi_con = ""
print("Chuỗi ký tự con chung của 2 chuỗi đã cho và có độ dài cực đại là:", max_chuoi)
"""

"""
Bài 10:
Cho trước chuỗi ký tự nhị phân bao gồm toàn các ký tự 0 và 1. 
Viết chương trình chuyển đổi số nhị phân này sang số thập phân.


n = input("Nhập vào một chuỗi nhị phân: ")
so_thap_phan = 0
so_mu = 0

# Duyệt qua từng chữ số nhị phân từ phải sang trái
for i in range(len(n) - 1, -1, -1):
    if n[i] == "1":
        so_thap_phan += 2 ** so_mu
    so_mu += 1

print("Số thập phân chuyển từ số nhị phân ban đầu là:", so_thap_phan)

1010 = 2^1 + 2^3 = 10
1111 = 2^0 + 2^1 + 2^2 + 2^3 = 15
"""

"""
Bài 12 bài tập mẫu:
Cho trước 2 chuỗi ký tự S1, S2 (giá trị có thể được nhập vào từ bàn phím). 
Viết chương trình thực hiện các yêu cầu sau:
a) Kiểm tra xem chuỗi ký tự S2 có nằm trong chuỗi ký tự S1 không?
b) Nếu có thì chuỗi ký tự S2 được xuất hiện (có thể không chồng lên nhau) trong chuỗi ký tự S1 bao nhiêu lần?
c) Tương tự câu b nhưng chỉ tính số lần xuất hiện chuỗi ký tự S2 trong chuỗi ký tự S1 không chồng lên nhau.
"""

str1 = input("Nhập vào chuỗi thứ nhất: ")
str2 = input("Nhập vào chuỗi thứ hai: ")
kiem_tra = str2 in str1 
if kiem_tra:
    a = str1.count(str2)
    print(a)
    
