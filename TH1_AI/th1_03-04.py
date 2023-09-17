import Ghifile as gf
import calculate as cal

size = gf.WriteF2()
array = gf.readFile2()

tong = 0

for i in array:
    for j in i:
        if cal.soNguyenTo(int(j)) == True:
            tong +=1

print("So nguyen to co trong array1: %2d" %tong)