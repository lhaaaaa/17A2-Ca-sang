"""
Bài 8: 
a) Viết chương trình sử dụng dictionary lưu các thông tin về tivi bao gồm (Hãng, model, năm sản xuất). In nội dung thông tin ra màn hình.
b) Giả sửa một từ điển (dictionary) lưu các thông tin khóa (key) về tivi bao gồm (Hãng, model, năm sản xuất). Viết chương trình kiểm tra một key có tồn tại trong từ điển không?

dict1 = {"tivi1": {"hang": "LG", "model": "ABC", "namsx": 2020},
         "tivi2": {"hang": "Sony", "model": "DEF", "namsx": 2021}}
print("tivi1" in dict1)  # True
print("tivi3" in dict1) # False
print("hang" in dict1["tivi1"]) # True
"""

"""
Bài 9: 
Giả sử đã có một dữ liệu từ điển thông tin học sinh bao gồm cặp <key>: <value>  là <Họ tên>: <Điểm số>. 
Chẳng hạn bộ dữ liệu gốc là: Dic = {"Nguyễn Văn A":9,0, "Lê Thị B":8.5}
Viết một chương trình có chức năng cập nhật điểm số sinh viên vào bộ dữ liệu đã có trên. Chương trình được thực hiện như sau:
+ Hai tham số được lần lượt nhập vào: Nhập họ tên sinh viên và Nhập điểm số.
+ Các thông tin trên sẽ được cập nhật vào bộ dữ liệu gốc, hoặc tạo mới một bản ghi, hoặc cập nhật chỉnh sửa điểm của sinh viên đã có trong danh sách. 
Chương trình sẽ đưa ra thông báo như sau: Đã tạo mới thêm dữ liệu họ tên và điểm một sinh viên hoặc Đã cập nhật lại thông tin điểm của sinh viên này.

thong_tin_sv = {"Nguyễn Văn A": 9.0, "Lê Thị B": 5.5, "Trần Văn C": 10.0}
# Tạo mới dữ liệu 
print("Đã tạo mới, thêm thông tin vào dữ liệu:")
thong_tin_sv["Đỗ Thị D"] = 9.5
print(thong_tin_sv)
# Cập nhật lại thông tin điểm sinh viên
print("Đã cập nhật lại thông tin điểm sinh viên:")
thong_tin_sv['Nguyễn Văn A'] = 8.0
print(thong_tin_sv)
"""

"""
Bài 10: Một từ điển D được định nghĩa bao gồm Khóa là mã sinh viên trong lớp, value là cặp 3 giá trị tên, điểm HP1, điểm HP2. 
Ví dụ: D = {"K1701":['Hà', 7,9.5], "K1702": ['Bình',10,8], "K1703":['Hoa', 6.0,9]}
Viết chương trình nhập bộ dữ liệu từ điển trên như sau:
+ Đầu tiên yêu cầu người dùng nhập mã sinh viên.
+ Tiếp theo yêu cầu nhập, tên, điểm HP1 và điểm HP2 trên một dòng bởi 1 chuỗi ký tự, và 2 số, cách nhau bởi dấu phẩy.
+ Thông báo loại 1: "Đã hoàn thành nhập điểm cho sinh viên mới.”
+ Thông báo loại 2: "Đã hoàn thành cập nhật lại nhập điểm cho sinh viên trong danh sách."
Bài 11: Viết chương trình tính điểm trung bình của K17 và in ra màn hình nội dung như sau:
K1701
Hà: 8.25
K1702
Bình: 9.0

dict1 = {}
while True:
    msv = input("Nhập mã sinh viên: ")
    if msv == "0":
        break
    ten, hp1, hp2, hp3 = map(str, input("Nhập thông tin về tên, điểm hp1 và điểm hp2: ").split(","))
    list_thong_tin = []
    list_thong_tin.append(ten)
    list_thong_tin.append(hp1)
    list_thong_tin.append(hp2)
    list_thong_tin.append(hp3)
    dict1[msv] = list_thong_tin
print(dict1)
dict2 = dict1.copy()
for key in dict2:
    tong = 0
    dict2[key].pop(0)
    for i in dict2[key]:
        diem = float(i)
        tong += diem
    diem_trung_binh = tong/len(dict2[key])
    print(f"Với mã sinh viên {key}, sinh viên {dict1[key][0]} có điểm trung bình là {diem_trung_binh}")
"""

"""
Bài 12: Cho trước một đoạn mã văn bản tiếng Anh:
Str = " Glucose is the fundamental thing that burns energy in our bodies. 
We get glucose from the foods we eat and it is transmitted to all cells via 
blood. This way, glucose ensures the energy which the cell needs. 
The quantity of the glucose in our blood shows us some data about our body's 
health. Measuring blood glucose level is the most common way to 
control people's medical condition."
Viết chương trình đếm xem đoạn văn bản trên có bao nhiêu từ và tần suất xuất hiện các từ trong chuỗi Str.

text = '''
Glucose is the fundamental thing that burns energy in our bodies. 
We get glucose from the foods we eat and it is transmitted to all cells via 
blood. This way, glucose ensures the energy which the cell needs. 
The quantity of the glucose in our blood shows us some data about our body's 
health. Measuring blood glucose level is the most common way to 
control people's medical condition.
'''
# Loại bỏ dấu câu
text = text.replace(".", " ")
text = text.replace(",", " ")
text = text.replace("'s", " ")
# Chuyển về chữ thường
text = text.lower()
print(text)
word_list = text.split()
word_count = {}
# Đếm số lượng từ và tần suất xuất hiện
for i in range(len(word_list)):
    count = 0
    for j in range(len(word_list)):
        if word_list[i] == word_list[j]:
            count += 1
    word_count[word_list[i]] = count
print("Tần suất xuất hiện của các từ trong đoạn văn là:")
print(word_count)
# Đếm số lượng từ trong đoạn văn:
print("Số lượng từ trong đoạn văn là:", len(word_count))
"""
