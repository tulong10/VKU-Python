import numpy as np
# Compute outer product of vectors
v = np.array([1,2,3]) # Tạo mảng numpy 1 chiều với 3 phần tử
w = np.array([4,5]) # Tạo mảng numpy 1 chiều với 2 phần tử
print(np.reshape(v, (3, 1)) * w) # Tính tích ngoài của v và w sử dụng broadcasting
# broadcasting là kỹ thuật trong numpy cho phép thực hiện các phép toán giữa các mảng có kích thước khác nhau bằng cách tự động mở rộng các mảng nhỏ hơn để phù hợp với kích thước của mảng lớn hơn.
x = np.array([[1,2,3], [4,5,6]]) # Tạo mảng numpy 2 chiều 2x3
print(x + v) # In  mảng x sau khi cộng với v
print((x.T + w).T)# In mảng x sau khi cộng với w sử dụng chuyển vị
print(x + np.reshape(w, (2, 1)))# In mảng x sau khi cộng với w sử dụng reshape
 # reshape là hàm trong numpy dùng để thay đổi hình dạng của mảng mà không làm thay đổi dữ liệu bên trong nó.