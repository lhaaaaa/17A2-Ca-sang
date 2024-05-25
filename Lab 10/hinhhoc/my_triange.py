def is_tamgiac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def chu_vi_tam_giac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        p = a + b + c
        return p
    else:
        print("3 cạnh không tạo thành tam giác")

def dien_tich_tam_giac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        p = a + b + c
        nua_chu_vi = p/2
        s = (nua_chu_vi*(nua_chu_vi-a)*(nua_chu_vi-b)*(nua_chu_vi-c))**0.5
        return s
    else:
        print("3 cạnh không tạo thành tam giác")