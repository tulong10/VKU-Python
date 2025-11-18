import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) # Tạo mảng numpy 2 chiều 4x3
v = np.array([1, 0, 1]) # Tạo mảng numpy 1 chiều với 3 phần tử
y = x + v # Cộng mảng v vào mảng x sử dụng broadcasting
print(y) # In mảng y sau khi cộng