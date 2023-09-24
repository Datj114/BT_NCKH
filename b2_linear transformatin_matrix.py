import numpy as np
A=np.array([[1,2,3],[4,5,6],[1,1,0]])
B=np.array([[1,1],[2,2],[1,1]])
x=np.array([2,2,2])
def multiply_matrix(A,B):
    return A@B
def inverse_matrix(A):
    return np.linalg.pinv(A)
# np.linalg: module trong np cho phép toán đại số tuyến tính và ma trận
# pinv viết tắt pseudo inverse
def det_matrix(A):
    return np.linalg.det(A)
def multiply_Ax(A,x):
    return A@x
print(multiply_Ax(A,x))
print(multiply_matrix(A,B))
print(det_matrix(A))
print(inverse_matrix(A))