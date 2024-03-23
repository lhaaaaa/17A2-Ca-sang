# Bài 1: Viết chương trình tính tổng của dãy các số từ 1 đến 200
#sum = 0
#for i in range(1,11):
#    sum = sum + i
#print(sum)

# Bài 2: Viết chương trình in ra màn hình dãy số lẻ bé hơn một số n nào đó được nhập vào từ bàn phím
#n = int(input("Nhập vào số n: "))
#print(f"Các số lẻ bé hơn {n} là:")
#for i in range(n):
#    if i % 2 != 0:
#        print(i)


# Bài 7: Vẽ hình tam giác 
n = int(input("Nhập vào chiều cao của tam giác: "))
# Câu a
#for i in range(1, n+1):
#    print("* " * i)
# Câu c
#for i in range(1, n+1):
#    # In ra khoảng trắng của mỗi dòng
#    for j in range(n - i):
#        print(' ', end="")
#    # In ra ký tự * cho tam giác
#    for j in range(i):
#        print("* ", end ='')
#    # Xuống dòng
#    print()
# Câu b
for i in range(n):
    # In ra khoảng trắng của mỗi dòng
    for j in range(n - i - 1):
        print(' ', end="")
    # In ra ký tự * cho tam giác
    for j in range(i+1):
        print("*", end ='')
    # Xuống dòng
    print()