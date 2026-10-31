import numpy as np

print("--- không seed ---")
print(np.random.rand(2))

print("--- có seed 42 ---")
np.random.seed(42)
print(np.random.rand(2))