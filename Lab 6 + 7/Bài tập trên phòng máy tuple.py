"""
Bài 14:
Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, 
name là string, age và score là number. Tuple được nhập vào bởi người dùng. 
Tiêu chí sắp xếp là: 
+ Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. 
+ Ưu tiên là tên > tuổi > điểm.
"""
thong_tin = []
while True:
    q = int(input("Nhập số thứ tự của sinh viên: "))
    if q == 0:
        break
    name = input("Nhập tên sinh viên: ")
    age = int(input("Nhập tuổi sinh viên: "))
    score = float(input("Nhập điểm sinh viên: "))
    tuple_sv = (name,)+ (age,) + (score,)
    thong_tin.append(tuple_sv)
print(thong_tin)
# Sắp xếp theo kiểu Bubble Sort
n = len(thong_tin)
for i in range(n-1):
    for j in range(n-i-1):
        if thong_tin[j][0] > thong_tin[j+1][0]:
            thong_tin[j], thong_tin[j+1] = thong_tin[j+1], thong_tin[j]
        elif thong_tin[j][0] == thong_tin[j+1][0]:
            if thong_tin[j][1] > thong_tin[j+1][1]:
                thong_tin[j], thong_tin[j+1] = thong_tin[j+1], thong_tin[j]
            elif thong_tin[j][1] == thong_tin[j+1][1]:
                if thong_tin[j][2] > thong_tin[j+1][2]:
                    thong_tin[j], thong_tin[j+1] = thong_tin[j+1], thong_tin[j]
print(thong_tin)

