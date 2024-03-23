# Bài 1:
#n = int(input("Nhập vào số n: "))
#a = 1 
#sum = 1
#for i in range(n):
#    a = a * (2*(i + 1)/(2*i + 3))
#    sum = sum + a
#print("Giá trị của biểu thức là:", sum)

# Bài 2: Viết chương trình tìm các số hoàn hảo nhỏ hơn n (Với n được nhập từ bàn phím)
#n = int(input("Nhập số n: "))
#print(f"Các số hoàn hảo nhỏ hơn {n} là:")
#for i in range(1,n):
    # Kiểm tra số i có phải là số hoàn hảo không?
#    sum = 0 
#    for j in range(1,i):
#        if i % j == 0:
#            sum = sum + j
#    if sum == i:
#        print(i)

# Bài 3: 
#1. Viết chương trình xét xem một số n có phải là số nguyên tố không. Nếu không phải hãy in ra số nguyên tố gần n nhất
#n = int(input("Nhập vào số n: "))
#if n <= 1:
#    print("Nhập lại số n")
#else:
    #Kiểm tra n có phải là số nguyên tố không? 
#    check = True 
#    for i in range(2,n): 
#        if n % i == 0: 
#            check = False
#    if check == True:
#        print(f"{n} là số nguyên tố")
#    else:
#        for j in range(n-1, 2, -1):
            #Kiểm tra từng số j có phải là số nguyên tố không?
#            check = True
#            for k in range(2,j):
#                if j % k == 0:
#                    check = False
#            if check == True: 
#                print(f"{j} là số nguyên tố nhỏ hơn {n} và gần {n} nhất")
#                break
#2. Viết chương trình in ra tất cả các số nguyên tố bé hơn hoặc bằng n
#n = int(input("Nhập vào số n: "))
#print(f"Các số nguyên tố bé hơn hoặc bằng {n} là:")
#if n <= 1:
#    print("Nhập lại số n")
#else:
#    for i in range(2,n+1):
        # Kiểm tra số i có phải là nguyên tố?
#        check = True 
#        for j in range(2,i):
#            if i % j == 0:
#                check = False
#        if check == True:
#            print(i)

# Bài 4
# Vẽ hình chữ nhật
#a = int(input("Nhập vào số hàng: "))
#b = int(input("Nhập vào số cột: "))
#for i in range(1,a+1):
#    for j in range(1,b+1):
#        print("* ", end ='')
#    print()

# Tam giác rỗng
n = int(input("Nhập chiều cao: "))
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end = '')
        else:
            print(' ', end ="")
    print()