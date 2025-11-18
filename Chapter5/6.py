import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) # Khai báo mảng numpy 2 chiều 4x3
print(a) # In mảng a
print ("-----------")
b = np.array([0, 2, 0, 1]) # Khai báo mảng b để chọn cột từ mảng a
print(a[np.arange(4), b]) # Lấy các phần tử ở vị trí (0,0), (1,2), (2,0), (3,1)
print ("----")
a[np.arange(4), b] += 10 # Tăng giá trị các phần tử ở vị trí (0,0), (1,2), (2,0), (3,1) lên  thêm 10
print(a) # In mảng a sau khi thay đổi giá trị
 # np.arange là hàm tạo mảng với các giá trị liên tiếp từ 0 đến n-1