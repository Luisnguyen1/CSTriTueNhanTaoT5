import Ghifile as gf
import calculate as cal

size = gf.WriteF2()
array = gf.readFile2()

tong = 0
flag = 0
col = 0

# while flag < size:        
#     for j in range(0,10):
#         if flag == size:
#             break
#         if cal.soNguyenTo(array[col][j]):
#             tong +=1
#         flag+=1
#     col+=1
# print("So luong so nguyen to trong matrix la: %2d"  %tong)

print(array)