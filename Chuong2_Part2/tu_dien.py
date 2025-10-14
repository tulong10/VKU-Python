def Tao_TD (Max):
    Tu_Dien ={}
    values = 0
    for i in range (1, Max +1):
        values = i ** 2
        Tu_Dien[i]= (values)
    return (Tu_Dien)
def pirnt_Item (Tu_Dien):
    for key , values in Tu_Dien.items():
        print (key, values)

def print_Keys (Tu_Dien):
    for key in Tu_Dien.keys():
        print (key)
def print_Values (Tu_Dien):
    for values in Tu_Dien.values():
        print (values)