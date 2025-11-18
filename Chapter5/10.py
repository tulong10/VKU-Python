import numpy as np
x = np.array([[1,2],[3,4]]) # Tao mảng numpy 2 chiều 2x2
y = np.array([[5,6],[7,8]]) # Tao mảng numpy 2 chiều 2x2
v = np.array([9,10]) # Tao mảng numpy 1 chiều với 2 phần tử
w = np.array([11, 12]) # Tao mảng numpy 1 chiều với 2 phần tử
print(v.dot(w)) # In tích vô hướng của v và w
print(np.dot(v, w)) # In tích vô hướng của v và w sử dụng hàm np.dot
print(x.dot(v)) # In tích của mảng x với v
print(np.dot(x, v)) # In tích của mảng x với v sử dụng hàm np.dot
print(x.dot(y)) # In tích của mảng x với y
print(np.dot(x, y)) # In tích của mảng x với y sử dụng hàm np.dot