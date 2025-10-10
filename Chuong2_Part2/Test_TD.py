from tu_dien import * 
max = int (input ("Nhap phan tu max cua tu dien:"))
TD = Tao_TD (max)
print ("Cac phan tu trong tu dien la:")
pirnt_Item (TD)
print ("Cac key trong tu dien la:")
print_Keys (TD)
print ("Cac values trong tu dien la:")
print_Values (TD)