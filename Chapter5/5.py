import numpy as np
a = np.array([[1,2], [3, 4], [5, 6]]) # Khai báo mảng numpy 2 chiều 3x2
print(a[[0, 1, 2], [0, 1, 0]]) # Lấy các phần tử ở vị trí (0,0), (1,1), (2,0)
print(np.array([a[0, 0], a[1, 1], a[2, 0]])) # Lấy các phần tử ở vị trí (0,0), (1,1), (2,0)
print(a[[0, 0], [1, 1]]) # Lấy các phần tử ở vị trí (0,1), (0,1)
print(np.array([a[0, 1], a[0, 1]])) # Lấy các phần tử ở vị trí (0,1), (0,1)