import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) # Khai báo mảng numpy 2 chiều 3x4
row_r1 = a[1, :] # Lấy hàng thứ 1 của mảng a
row_r2 = a[1:2, :] # Lấy hàng thứ 1 của mảng a nhưng vẫn giữ nguyên dạng 2 chiều
print(row_r1, row_r1.shape) # In hàng row_r1 và kích thước của nó
print(row_r2, row_r2.shape) # In hàng row_r2 và kích thước của nó
col_r1 = a[:, 1] # Lấy cột thứ 1 của mảng a
col_r2 = a[:, 1:2] # Lấy cột thứ 1 của mảng a nhưng vẫn giữ nguyên dạng 2 chiều
print(col_r1, col_r1.shape) # In cột col_r1 và kích thước của nó
print(col_r2, col_r2.shape) # In cột col_r2 và kích thước của nó