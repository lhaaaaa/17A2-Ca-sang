def cong_ma_tran(A, B):
    if len(A) != len(B) and len(A[0]) != len(B[0]):
        print("Hai ma trận không thực hiện được phép cộng")
    else:
        C = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                row.append(A[i][j] + B[i][j])
            C.append(row)
        return C
    
def tru_ma_tran(A, B):
    if len(A) != len(B) and len(A[0]) != len(B[0]):
        print("Hai ma trận không thực hiện được phép trừ")
    else:
        C = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                row.append(A[i][j] - B[i][j])
            C.append(row)
        return C
    
def nhan_ma_tran(A, B):
    if len(A[0]) != len(B):
        print("Hai ma trận không thực hiện được phép nhân")
    else:
        C = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                total = 0
                for k in range(len(B)):
                    total += A[i][k]*B[k][j]
                row.append(total)
            C.append(row)
        return C
        