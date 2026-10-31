import numpy as np

scores = np.array([5, 8, 3, 9, 6])
M = np.array([[1, 2, 3], [4, 5, 6]])

# 1. In shape của M
print(M.shape)
# 2. In cột 2 của M
print(M[:,2])
# 3. In các điểm > 5
print(scores[scores>5])
# 4. In mọi điểm sau khi tăng 10%
print(scores * 1.1)