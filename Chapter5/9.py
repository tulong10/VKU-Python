import numpy as np
x = np.array([[1,2],[3,4]], dtype=np.float64) # Tạo mảng numpy 2 chiều 2x2 với kiểu dữ liệu float64
y = np.array([[5,6],[7,8]], dtype=np.float64) # Tạo mảng numpy 2 chiều 2x2 với kiểu dữ liệu float64
print(x + y) # In tổng của hai mảng x và y
print(np.add(x, y)) # In tổng của hai mảng x và y sử dụng hàm np.add
print(x - y) # In hiệu của hai mảng x và y
print(np.subtract(x, y)) # In hiệu của hai mảng x và y sử dụng hàm np.subtract
print(x * y) # In tích của hai mảng x và y
print(np.multiply(x, y)) # In tích của hai mảng x và y sử dụng hàm np.multiply
print(x / y) # IN chia của hai mảng x và y
print(np.divide(x, y)) # In chia của hai mảng x và y sử dụng hàm np.divide
print(np.sqrt(x)) # In căn bậc hai của mảng x sử dụng hàm np.sqrt