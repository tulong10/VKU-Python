import numpy as np
x = np.array([[1,2],[3,4]]) # Tạo mảng numpy 2 chiều 2x2
print(np.sum(x)) # Tính tổng tất cả các phần tử trong mảng x
print(np.sum(x, axis=0)) # In tổng các phần tử theo cột
print(np.sum(x, axis=1)) # In tổng các phần tử theo hàng
x = np.array([[1,2], [3,4]]) # Tạo mảng numpy 2 chiều 2x2
print(x) # In mảng x
print(x.T) # In chuyển vị của mảng x
v = np.array([1,2,3]) # Tạo mảng numpy 1 chiều với 3 phần tử
print(v) # In mảng v
print(v.T) # In chuyển vị của mảng v (không thay đổi gì vì v là mảng 1 chiều)