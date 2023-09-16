import Ghifile as gf
import calculate as cal

size = gf.WriteF1()
array = gf.readFile1()
#----------------------------------------

print("----------------------TH-01----------------------------")
tong = 0
for a in array:
    for b in a:
        if cal.soNguyenTo(b):
            tong +=1
print("So luong so nguyen to trong matrix la: %2d"  %tong)
print("--------------------------------------------------")
i = 0
for a in array:
    tong = 0
    i += 1
    for b in a:
        tong = tong + b
    print("Tổng của dòng thứ%2d" %i + "= %2d" %tong)    
print("--------------------------------------------------")
tong = 0
i = 0
for a in range(0,size[1]):
    for b in range(0,size[0]):
        tong += array[b][a]
    print("Tổng của cột thứ%2d" %(a+1) + "= %2d" %tong) 
    tong = 0
print("--------------------------------------------------")
