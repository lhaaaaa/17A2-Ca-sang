# Khởi tạo và khai báo dictionary
#dict1 = {"a": 1, "b": 2, "c": 3}
#print(dict1)

# Sử dụng vòng lặp trong dictionary
# Lặp qua các key trong dictionary
#for key in dict1:
#    value = dict1[key]
#    print(value)

# Lặp qua cặp giá trị key-value trong dictionary
#for key, value in dict1.items():
#    print(f"Với key = {key} thì value = {value}")

# Khai báo một dictionary rỗng
#dict2 = {}
#dict3 = dict()
#print(dict2)
#print(dict3)

# Các thao tác cơ bản trên dictionary

# Thêm phần tử vào dictionary 
#dict1["d"] = 4 # Tạo một key mới trong dictionary
#print(dict1)

# Thay đổi giá trị (value) của một key trong dictionary
#dict1["d"] = 5 # Thay đổi giá trị của key trong dictionary
#print(dict1) 

# Truy cập vào giá trị của key trong dictionary -> Trả về value của key đó
#print(dict1["a"])
#print(dict1.get("b"))

# Xóa phần tử ra khỏi dictionary
# Sử dụng câu lệnh del
# del dict1 # Xóa sự hiện diện của dict1 trong bộ nhớ
# print(dict1)

# Sử dụng phương thức pop()
# print(dict1.pop("b")) # Lấy phần tử ra khỏi dictionary
# print(dict1) # In ra dictionay sau khi sử dụng phương thức pop

# Sử dụng phương thức popitem()
# print(dict1.popitem())
# print(dict1.popitem())
# print(dict1)

# Sử dụng clear()
# print(dict1.clear())
# print(dict1)

# Lấy danh sách các key trong dictionary
# print(dict1.keys())
# Lấy danh sách các value trong dictionary
# print(dict1.values())

# Tính số phần tử của dictionary
# print(len(dict1))

# Sao chép dictionary
# dic2 = dict1.copy()
# print(dic2)

# Tìm max của dictionary
# print(max(dict1)) 

# Hàm all()
#dict1 = {1: "True", "0": "False"}
#dict2 = {0: "True", 1: "False"}
#dict3 = {}
#dict4 = {"0": False}
#print(all(dict1))
#print(all(dict2))
#print(all(dict3))
#print(all(dict4))

# Hàm any()
#print(any(dict1))
#print(any(dict2))
#print(any(dict3))
#print(any(dict4))

# Ghép nối 2 dictionary
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"d": 4, "e": 5}
# dict1.update(dict2)
# print(dict1)
# print(dict2)
# dict1 | dict2
# print(dict1)
# print(dict2)

# Dictionary comprehension
numbers = [1, 2, 3, 4]
dict1 = {num: num ** 2 for num in numbers}
print(dict1)