"""
Bài 2:
Biết rằng dãy số Fibonacci là dãy số vô hạn, 
được bắt đầu bởi số 0 và số 1, các số tiếp theo luôn bằng tổng của 
1 số liền trước cộng lại.
Ví dụ: 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
Viết hàm tìm và in ra màn hình dãy Fibonacci không quá 10 số hạng 
(Hàm không có giá trị trả về)

def fib(n):
    lst_fib = [0,1]
    if n <= 1:
        return lst_fib[:n+1]
    while len(lst_fib) <= n:
        so_tiep_theo = lst_fib[-1] + lst_fib[-2]
        lst_fib.append(so_tiep_theo)
    return lst_fib

n = int(input("Nhập vào một số: "))
day_fib = fib(n)
print("Dãy fibonacci là:", day_fib)
"""

"""
Bài 3:
a) Viết chương trình (yêu cầu xây dựng hàm) để nhập số nguyên dương n. Kiểm tra n có phải là số nguyên tố không?
b) Viết chương trình, trong đó xây dưng hàm nhập số nguyên dương n. Kiểm tra n có phải là số hoàn hảo không?
c) Trong toán học số nguyên n gọi là số đối xứng nếu đọc từ trái qua phải, hay từ phải qua trái đều được số giống nhau. Ví dụ: 11, 121, 101 là các số đối xứng.
Viết chương trình (yêu cầu xây dựng hàm) in ra màn hình các số đối xứng trong phạm vi 1000. 
Quy cách in mỗi số đối xứng chiếm 05 ký tự và tối đa 15 số trên một hàng mới chuyển qua hàng mới.
"""

# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(a):
    if a < 2:
        return False
    else:
        for i in range(1, a):
            if a % i == 0:
                return False
        return True

# Hàm kiểm tra số hoàn hảo
def tim_uoc(n):
    tap_uoc = []
    for i in range(1, n):
        if n % i == 0:
            tap_uoc.append(i)
    return tap_uoc
def kiem_tra_so_hoan_hao(n):
    tap_uoc = tim_uoc(n)
    sum = 0
    for so in tap_uoc:
        sum += so
    if sum == n:
        return True
    else:
        return False
    
# Kiểm tra số đối xứng
def kiem_tra_so_doi_xung(n):
    so = n
    dao_nguoc = 0

    while so > 0:
        phan_du = so % 10
        dao_nguoc = dao_nguoc * 10 + phan_du
        so = so// 10

    if n == dao_nguoc:
        return True
    else:
        return False
    
# Chương trình chính
def main():
    n = int(input("Nhập vào số nguyên dương: "))
    if kiem_tra_so_nguyen_to(n):
        print(f"{n} là số nguyên tố")
    if kiem_tra_so_hoan_hao(n):
        print(f"{n} là số hoàn hảo")
    for i in range(1000):
        if kiem_tra_so_doi_xung(i):
            print(i, end = " ")

if __name__ == "__main__":
    main()