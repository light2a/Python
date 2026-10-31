import numpy as np

diem = np.array([[7, 8, 6, 9],
                 [5, 9, 8, 7],
                 [8, 6, 9, 10]])
#                 Toán Lý Hoá Anh

print(diem.shape)
print(diem[:, 1])
ly = diem[:, 1]
print(ly[ly >= 8])
print(diem[:, 1] * 2)