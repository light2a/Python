import numpy as np

# mỗi hàng = 1 căn nhà: [diện tích m2, số phòng ngủ, tuổi nhà]
X = np.array([
    [ 50, 1, 30],
    [ 80, 2, 10],
    [120, 3,  5],
    [ 65, 2, 20],
    [200, 4,  2],
], dtype=float)

print("X shape:", X.shape)

# TODO: tính mu = trung bình của TỪNG CỘT
mu = X.mean(axis=0)
print("mu:", mu)
print("mu shape:", mu.shape)
sigma = X.std(axis=0)
print("sigma:", sigma)
# TODO: chuẩn hoá
Z = (X - mu)/sigma
print("Z:")
print(Z)
print("Z shape:", Z.shape)

# TODO: kiểm tra
print("mean từng cột:", Z.mean(axis=0) )       # mean của Z theo axis=0
print("std  từng cột:", Z.std(axis=0))        # std của Z theo axis=0
print("mean ≈ 0?", np.allclose(Z.mean(axis=0), 0))
print("std  ≈ 1?", np.allclose(Z.std(axis=0), 1))