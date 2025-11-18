import numpy as np
v = np.array([1,2,3]) # Tạo mảng numpy 1 chiều với 3 phần tử
w = np.array([4,5]) # Tạo mảng numpy 1 chiều với 2 phần tử
print(np.reshape(v, (3, 1)) * w) # Tính tích ngoài của v và w sử dụng broadcasting
x = np.array([[1,2,3], [4,5,6]]) # Tạo mảng numpy 2 chiều 2x3
print(x + v) # In mảng x sau khi cộng với v
print((x.T + w).T) # In mảng x sau khi cộng với w sử dụng chuyển vị
print(x + np.reshape(w, (2, 1))) # In mảng x sau khi cộng với w sử dụng reshape
print(x * 2) # In mảng x sau khi nhân với 2