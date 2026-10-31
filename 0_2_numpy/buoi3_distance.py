import numpy as np
import time

np.random.seed(42)
P = np.random.rand(200_000, 2)   # 200.000 quán cà phê, mỗi hàng (x, y)
q = np.array([0.5, 0.5])         # vị trí của bạn

print("P shape:", P.shape)

# --- cách 1: vòng for ---
t0 = time.perf_counter()
d_loop = np.zeros(len(P))        # chuẩn bị sẵn 200.000 ô trống để ghi kết quả
for i in range(len(P)):
    # TODO: tính khoảng cách từ điểm P[i] tới q, rồi ghi vào d_loop[i]
    # P[i, 0] là x, P[i, 1] là y của điểm thứ i    
    d_loop[i] = np.sqrt((P[i, 0] - q[0])**2 + ( P[i, 1] - q[1])**2)
t1 = time.perf_counter()

print("for :", t1 - t0, "giây")
print("5 khoảng cách đầu:", d_loop[:5])

# --- cách 2: vector hoá ---
t2 = time.perf_counter()
d_vec = np.sqrt(((P - q)**2).sum(axis=1))                       # dòng ghép 4 mảnh ở trên
t3 = time.perf_counter()

print("vec :", t3 - t2, "giây")
print("nhanh hơn:", (t1 - t0)/(t3 - t2), "lần")

# --- kiểm tra 2 cách cho cùng kết quả ---
print("giống nhau?", np.allclose(d_loop, d_vec))

idx = np.argmin(d_vec)  
print("quán gần nhất: số", idx)
print("toạ độ:", P[d_vec.argmin()])
print("khoảng cách:", d_vec.min())