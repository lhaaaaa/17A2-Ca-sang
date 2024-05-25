def bac_nhat(a,b):
    if b != 0:
        return -b/a
    
def bac_hai(a,b,c):
    if a != 0:
        delta = b**2 - 4*a*c
        if delta == 0:
            nghiem = -b/(2*a)
            return nghiem, nghiem
        elif delta > 0:
            nghiem1 = (-b + delta**0.5)/2
            nghiem2 = (-b - delta**0.5)/2
            return nghiem1, nghiem2 