def ucln(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def bcnn(a,b):
    uoc_chung = ucln(a,b)
    boi_chung = (a*b)/uoc_chung
    return boi_chung

def tong_uoc(a):
    sum = 0
    for i in range(1,a+1):
        if a%i == 0:
            sum += i
    return sum
