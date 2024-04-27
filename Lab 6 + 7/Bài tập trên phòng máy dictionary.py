"""
Bài 2: 
Thống kê chiều cao của các học sinh trong nhóm sinh viên được kết quả như sau:
161 182 161 154 176 170 167 171 170 174 150 142 148 165 170 178 156 145 149 163
162 159 165 165 170 180 155 159 155 153 152 162 180 168 169 168 167 170. 
a) Hỏi nhóm có bao nhiêu sinh viên?
b) Tính chiều cao trung bình của các sinh viên trong nhóm.
c) Liệt kê các chiều cao khác nhau sinh viên trong nhóm.

thong_ke_chieu_cao = '''
161 182 161 154 176 170 167 171 170 174 150 142 148 165 170 178 156 145 149 163 162 159 165 165 170 180 155 159 155 153 152 162 180 168 169 168 167 170
'''
danh_sach_chieu_cao = []
thong_ke_chieu_cao = thong_ke_chieu_cao.split()
for chieu_cao in thong_ke_chieu_cao:
    chieu_cao = int(chieu_cao)
    danh_sach_chieu_cao.append(chieu_cao)
# Hỏi nhóm có bao nhiêu sinh viên?
print("Số lượng sinh viên có trong nhóm là:", len(thong_ke_chieu_cao))
# Tính chiều cao trung bình của các sinh viên trong nhóm
tong = 0
for chieu_cao in danh_sach_chieu_cao:
    tong += chieu_cao
print("Chiều cao trung bình của sinh viên là:", tong/len(thong_ke_chieu_cao))
# Liệt kê các chiều cao khác nhau sinh viên trong nhóm
dict1 = {}
for i in danh_sach_chieu_cao:
    count = 0
    for j in danh_sach_chieu_cao:
        if i == j:
            count += 1
    dict1[i] = count
print("Nhóm chiều cao khác nhau là:", dict1)
"""

"""
Bài 5: 
Viết chương trình nhập 2 số tự nhiên m, n. Tính tổng các chữ số chung của m và n. 
Ví dụ: m = 1123499, n = 112229; có chữ số chung là 1, 2, 9 do đó tổng các chữ số chung bằng 1+2+9 = 12. 
Trường hợp có một chữ số xuất hiện nhiều lần trong cả m và n thì chữ số đó chỉ được tính một lần.

m, n = map(int, input("Nhập vào 2 số tự nhiên: ").split())
# Chuyển các số thành dạng chuỗi
chuoi_m = str(m)
chuoi_n = str(n)
dict1 = {}
for i in chuoi_m:
    count = 0
    for j in chuoi_n:
        if i == j:
            count += 1
            dict1[i] = count
tong = 0
for key in dict1:
    tong += int(key)
print(f"Tổng các chữ số chung của 2 số {m} và {n} là {tong}")
"""