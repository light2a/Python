import numpy as np
import time

a = np.random.rand(1_000_000)
b = np.random.rand(1_000_000)

# --- vòng for ---
t0 = time.perf_counter()
total_loop = 0
for i in range(len(a)):
    total_loop += a[i] * b[i]
t1 = time.perf_counter()

# --- numpy ---
t2 = time.perf_counter()
total_np = np.dot(a, b)
t3 = time.perf_counter()

print("for  :", t1 - t0, "giây")
print("numpy:", (t3 -t2), "giây")
print("nhanh hơn:", (t1 - t0) / (t3 -t2), "lần")
print(total_loop == total_np)
print(np.isclose(total_loop, total_np))