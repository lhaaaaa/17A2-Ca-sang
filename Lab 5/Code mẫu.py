# Định nghĩa chuỗi
#a = "17A2 Ca sáng ngày 6/4/2024"
#print(type(a))

# Chỉ mục
# Truy cập từ đầu chuỗi
#a = "Hello"
#print(a[1])
#print(type(a[1]))

# Truy cập từ cuối chuỗi
#a = "fbsregnvbjgekrbhjklpkjhiohsjfeiogfeofollmmmmjiiieth94hwo53032t55903--579428f4"
#print(a[-2])

# Sử dụng slicing (lấy chuỗi con từ chuỗi ban đầu)
"""
a = "Khoa hoc du lieu"
print(a[2:6]) # Khuyết step
print(a[2:7:2]) # Có step
print(a[:5]) # Khuyết start
print(a[8:]) # Khuyết end
print(a[::-1]) #Khuyết start, khuyết end, step = -1  -> Đảo ngược chuỗi
"""

# Độ dài chuỗi (số ký tự có trong chuỗi)
#a = "fbsregnvbjgekrbhjklpkjhiohsjfeiogfeofollmmmmjiiieth94hwo53032t55903--579428f4"
#print(len(a))
# Sử dụng len() trong vòng lặp
#a = "Hello"
#for i in range(len(a)): #Truy cập vào từng CHỈ MỤC trong chuỗi
#    print(a[i], end = " ")

# Truy cập từng KÝ TỰ trong chuỗi
#for i in a:
#    print(i, end = " ")

# Các hàm cơ bản trong chuỗi
# lower()
            #a = "HEllo"
            #b = a.lower() #"hello"
# upper()
            #print(b.upper()) # "HELLO"
# strip()
            #a = "      658272    gjid        "
            #print(a.strip())
# split(ký tự phân cách)
            #a = "Khoa hoc du lieu"
            #print(a.split(" "))
            #b = "Khoa;hoc;du;lieu"
            #print(b.split(";"))
# replace(ký tự cũ, ký tự mới)
            #a = "Hello"
            #print(a.replace("l","n"))
# find(ký tự)
            #a = "abcaaaaa"
            #b = a.find("a") # Tìm chỉ mục của ký tự XUẤT HIỆN LẦN ĐẦU TIÊN trong chuỗi
            #print(type(b)) # Dạng của chỉ mục
            #print(a.find("d")) #Không tìm thấy ký tự trong chuỗi

# rfind(chuỗi con, bắt đầu, kết thúc)
            #a = "Khoa hoc du lieu"
            #print(a.rfind("hoc"))
            #print(a.rfind("hoc", 5))
            #print(a.rfind("hoc", 0, 5))
# count(ký tự)
            #a = "abcaabcaaa"
            #print(a.count("a"))
            #print(a.count("d"))

# chuỗi.isdigit()/chuỗi.isnumeric()
            #a = "125824"
            #print(a.isdigit())
            #print(a.isnumeric())
# chuỗi.isalpha()
            #a = "ABCirjr"
            #b = "ABFBonk9749"
            #print(a.isalpha())
            #print(b.isalpha())
# chuỗi.capitalize()
            #a = "hellO"
            #print(a.capitalize()) #Hello
# chuỗi.isupper()/chuỗi.islower()
            #a = "HELLO"
            #b = "hello"
            #c = "HEllo"
            #print(a.isupper()) #True
            #print(b.isupper()) #False
            #print(c.isupper()) #False
# Nối chuỗi 
# Sử dụng +
#a = "Hello"
#b = "Hi"
#print(a + " " + b)
#print(a + b)
# Sử dụng join
#print("".join([a,b]))