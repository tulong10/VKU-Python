import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) # Tạo mảng numpy 2 chiều 4x3
v = np.array([1, 0, 1]) # Tạo mảng numpy 1 chiều với 3 phần tử
vv = np.tile(v, (4, 1)) # Tạo mảng vv bằng cách lặp lại mảng v thành 4 hàng
print(vv) # In mảng vv
y = x + vv # Cộng mảng vv vào mảng x
print(y) # In mảng y sau khi cộng