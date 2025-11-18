import numpy as np
a = np.array([[1,2], [3, 4], [5, 6]]) # Khai báo mảng numpy 2 chiều 3x2
bool_idx = (a > 2) # Tạo mảng boolean với điều kiện các phần tử lớn hơn 2
print(bool_idx) # In mảng boolean
print(a[bool_idx]) # Lấy các phần tử của mảng a thỏa mãn điều kiện
print(a[a > 2]) # Cách viết ngắn gọn hơn để lấy các phần tử thỏa mãn điều kiện