
month = int(input("Nhập so thang (vd : 1,3,5,...): "))

if month in (1,3,5,7,8,10,12):
    print(f"Tháng {month} có 31 ngày.")
elif month in (4,6,9,11):
    print(f"Tháng {month} có 30 ngày.")
elif month == "2":
    print(f"Tháng {month} có 28 hoặc 29 ngày (năm nhuận).")
else:
    print("Lỗi: Tên tháng không hợp lệ. Vui lòng nhập đúng tên tháng tiếng Anh.")
