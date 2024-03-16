# Bài 1
"""
Viết chương trình nhập vào một tháng và cho biết tháng đó có bao nhiêu ngày?
Bước 1: Nhập vào 1 tháng, nhập vào năm
Bước 2: Kiểm tra điều kiện:
Tháng 4, 6, 9, 11 là những tháng có 30 ngày
Tháng 1, 3, 5, 7, 10, 12 là những tháng có 31 ngày
Tháng 2: kiểm tra điều kiện của năm
   + Năm nhuận: tháng có 29 ngày
   + Năm không nhuận: tháng có 28 ngày
"""

# Bài 4
# Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra 0.
#n = int(input("Nhập vào một số nguyên: "))
#if 100 <= n <= 999:
#    chu_so_hang_tram = n // 100
#    print("Chữ số hàng trăm của số {} là {}".format(n, chu_so_hang_tram))

# Bài 10
"""
Một điểm cho thuê sân tập bóng đá theo công thức sau:
+ Mỗi giờ trong 3 giờ đầu tiên tính 100.000 đồng/ giờ
+ Mỗi giờ tiếp theo có đơn giá giảm 25% so với đơn giá trong 3 giờ đầu tiên
+ Ngoài ra nếu thời gian thuê sân từ 11 giờ đến 15 giờ thì được giảm giá 10%
Viết chương trình nhập vào giờ bắt đầu, giờ kết thúc và in ra số tiền khách thuê sân tập phải trả, biết rằng 5 giờ <= giờ bắt đầu <= giờ kết thúc <= 22 giờ
"""
gio_bat_dau = int(input("Nhập giờ vào: "))
gio_ket_thuc = int(input("Nhập giờ ra: ")) 
gio_thue = gio_ket_thuc - gio_bat_dau + 1
tien_thue = 0
if gio_bat_dau < 5 and gio_ket_thuc > 22:
    print("Giờ thuê không thỏa mãn")
else:
    if gio_thue < 3:
        if 11 <= gio_bat_dau <= gio_ket_thuc <= 15:
            tien_thue = 100000*gio_thue - (100000*gio_thue)*0.1
        else:
            tien_thue = 100000*gio_thue
    else: 
        if 11 <= gio_bat_dau <= gio_ket_thuc <= 15:
            tien_thue = 100000*gio_thue - (100000*gio_thue)*0.1 - (100000*(gio_thue - 3)*0.25)
        else:
            tien_thue = 100000*gio_thue - (100000*(gio_thue - 3)*0.25)
    print("Tiền thuê sân là:", tien_thue)