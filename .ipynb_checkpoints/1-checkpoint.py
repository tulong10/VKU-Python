import numpy as np 
a = np.array([1,2,3]) # Khai báo mảng numpy có 3 phần tử
print (type(a)) # In kiểu dữ liệu của a
print (a.shape) # In kích thước của mảng a
print (a[0], a[1], a[2]) # In các phần tử trong mảng a
a[0] = 5 # Thay đổi giá trị phần tử đầu tiên của mảng a
print (a) # In mảng a sau khi thay đổi giá trị
b = np.array([[1,2,3],[4,5,6]]) # Khai báo mảng numpy 2 chiều 2x3
print (b.shape) # In kích thước của mảng b
print (b[0,0], b[0,1], b[1,0])  # In các phần tử trong mảng b