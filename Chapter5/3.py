import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) # Khai báo mảng numpy 2 chiều 3x4
b = a[:2, 1:3] # Lấy một phần của mảng a theo hàng và cột, :2 là lấy 2 hàng đầu tiên, 1:3 là lấy cột 1 và 2
print (b) # In mảng b
print(a[0, 1]) # In phần tử ở hàng 0, cột 1 của mảng a
b[0, 0] = 77 # Thay đổi giá trị phần tử ở hàng 0, cột 0 của mảng b
print(a[0, 1]) # In lại phần tử ở hàng 0, cột 1 của mảng a để thấy sự thay đổi