import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) # Tạo mảng numpy 2 chiều 4x3
v = np.array([1, 0, 1]) # Tạo mảng numpy 1 chiều với 3 phần tử
y = np.empty_like(x) # Tạo mảng y có cùng kích thước với x nhưng chưa khởi tạo giá trị
for i in range(4): # Lặp qua từng hàng của mảng x
    y[i, :] = x[i, :] + v # Cộng mảng v vào mỗi hàng của mảng x và gán kết quả vào mảng y
print(y) # In mảng y sau khi cộng