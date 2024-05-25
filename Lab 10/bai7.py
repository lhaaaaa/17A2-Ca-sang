def sinh_ngau_nhien():
    import random
    random_numbers = [random.randint(1, 100) for _ in range(100)]
    return random_numbers

def so_nguyen_to(a):
    if a < 2:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    
def so_chinh_phuong(a):
    if int(a) == int((a**0.5)**2):
        return True
    else:
        return False
    
def chia_het_7(random_numbers):
    lst = []
    for so in random_numbers:
        if so_nguyen_to(so):
            if so % 7 == 0:
                lst.append(so)
    return lst

def lst_chinh_phuong(random_numbers):
    lst = []
    for so in random_numbers:
        if so_chinh_phuong(so):
            lst.append(so)
    return lst