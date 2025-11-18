import numpy as np
x = np.array([1, 2]) # Tạo mảng numpy 1 chiều với các phần tử là 1 và 2
print(x.dtype) # In kiểu dữ liệu của các phần tử trong mảng x
x = np.array([1.0, 2.0]) # Tạo mảng numpy 1 chiều với các phần tử là 1.0 và 2.0
print(x.dtype) # In kiểu dữ liệu của các phần tử trong mảng x
x = np.array([1, 2], dtype=np.int64) # Tạo mảng numpy 1 chiều với các phần tử là 1 và 2, kiểu dữ liệu int64
print(x.dtype) # In kiểu dữ liệu của các phần tử trong mảng x
# dtype=np.int64 Là tham số để chỉ định kiểu dữ liệu của các phần tử trong mảng numpy, cũng có thể ép kiểu dữ liệu khác như np.float32, np.float64, np.complex. ..