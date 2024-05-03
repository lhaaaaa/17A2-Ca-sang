"""
Bài 9: 
Cho trước một tuple chứa các số tự nhiên sau (1,2,3,4,5,6,7,8,9,10,11)
Viết chương trình lưu nửa đầu và nửa cuối của tuple trên vào các tuple tp1 
và tp2. In kết quả ra màn hình.

tuple_ban_dau = (1,2,3,4,5,6,7,8,9,10,11)
vi_tri_giua = int(len(tuple_ban_dau)/2)
tp1 = tuple_ban_dau[:vi_tri_giua]
tp2 = tuple_ban_dau[vi_tri_giua:]
print(tp1)
print(tp2)
"""

"""
Bài 10: 
Viết chương trình tạo một tuple chứa toàn các số lẻ được lọc ra từ tuple 
cho trước 
tp = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 

tp = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 
tp_new = ()
for element in tp:
    if element % 2 != 0:
        tp_new = tp_new + (element,)
print(tp_new)
"""