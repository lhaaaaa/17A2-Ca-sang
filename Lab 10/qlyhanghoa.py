def nhapthongtin():
    ma_hang = input("Nhập mã hàng: ")
    ten_hang = input("Nhập tên hàng: ")
    don_vi_tinh = input("Nhập đơn vị tính: ")
    don_gia = int(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng hàng: "))
    return ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong

def thanhtien(don_gia, so_luong):
    thanh_tien = don_gia*so_luong
    return thanh_tien

def thue(thanh_tien):
    tien_thue = thanh_tien * 0.1
    return tien_thue
