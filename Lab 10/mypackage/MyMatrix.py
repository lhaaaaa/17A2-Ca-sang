def isMatrix(A): #Kiểm tra có phải là ma trận
    if len(A) < 2:
        return False
    row_length = len(A[0])
    return all(len(row) == row_length for row in A)

def inMatrix(A): #In ra ma trận
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end = " ")
        print()

def isSquare(A): #Kiểm tra ma trận vuông
    if len(A) != len(A[0]):
        return False
    return True

def changeRow(A, row1, row2): #Tráo đổi 2 hàng
    if row1 < 0 or row1 >= len(A) or row2 < 0 or row2 >= len(A):
        return False
    #Lưu trữ biến A[row1]
    temp = A[row1]
    #Thay đổi vị trí 2 hàng
    A[row1] = A[row2]
    A[row2] = temp
    return True
 
def changeCol(A, col1, col2): #Tráo đổi 2 cột
    if col1 < 0 or col1 >= len(A[0]) or col2 < 0 or col2 >= len(A[0]):
        return False
    for row in range(len(A)):
        A[row][col1], A[row][col2] = A[row][col2], A[row][col1]
    return True

def transpose(A): #In ra ma trận chuyển vị
    #Tạo ma trận chuyển vị rỗng
    transpose = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    #Điền các giá trị cho ma trận chuyển vị
    for i in range(len(A)):
        for j in range(len(A[0])):
            transpose[j][i] = A[i][j]
    return transpose

def GetSymetry(A): #Kiểm tra ma trận đối xứng
    if len(A) != len(A[0]):
        return False
    else:
        for i in range(len(A)):
            for j in range(i, len(A[0])):
                if A[i][j] != A[j][i]:
                    return False
        return True