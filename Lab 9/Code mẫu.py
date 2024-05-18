"""
# Hàm đệ quy 
def factorial(n):
    if n == 0:
        return 1  # Điều kiện cơ sở: giai thừa của 0 là 1
    else:
        return n * factorial(n - 1)  # Điều kiện dừng: nếu n > 0, tiếp tục đệ quy
result = factorial(5)
print(result)
"""
# Bài toán tính giai thừa
import time
# Cách 1: Không dùng hàm
n = 1000
start1 = time.time()
tich1 = 1 
for i in range(1,n+1):
    tich1 *= i
print(tich1)
end1 = time.time() 
print("Thời gian chạy Cách 1:", end1 - start1)

# Cách 2: Dùng hàm thông thường
def giai_thua1(n):
    tich2 = 1
    for i in range(1,n+1):
        tich2 *= i
    return tich2
start2 = time.time()
tich2 = giai_thua1(n)
print(tich2)
end2 = time.time()
print("Thời gian chạy Cách 2:", end2 - start2)

# Cách 3: Dùng hàm đệ quy 
def giai_thua2(n):
    if n == 0:
        return 1  
    else:
        return n * giai_thua2(n - 1)
start3 = time.time()
tich3 = giai_thua2(n)
print(tich3)
end3 = time.time()
print("Thời gian chạy Cách 3:", end3 - start3)