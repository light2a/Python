import numpy as np

A = np.ones((4, 3))
b = np.array([10, 20, 30])
c = np.array([[1], [2], [3], [4]])

print("1. A + b:", (A + b).shape)
print("2. A + c:", (A + c).shape)
print("3. A.sum(axis=0):", A.sum(axis=0).shape)
print("4. A.sum(axis=1):", A.sum(axis=1).shape)
print("5. A.reshape(2, 6):", A.reshape(2, 6).shape)
print("6. A.reshape(-1):", A.reshape(-1).shape)
print("7. A.T:", A.T.shape)
print("8. A + np.array([1, 2, 3, 4])", A + np.array([1, 2, 3, 4]))