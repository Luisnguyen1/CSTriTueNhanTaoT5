import numpy as np
def WriteF1():
    print("Nhap m:", end=" ")
    m = int(input())

    print("Nhap n:", end=" ")
    n = int(input())

    array = []

    for i in range (0,m):
        array.append([])
        for j in range(0,n):
            x = int(input("Nhap phan tu thu [%2d][%2d]: "%(i+1, j+1)))
            array[i].append(x)

    f = open("./TH1_AI/array2.txt ","w")

    for i in range (0,m):
        for j in range(0,n):
            f.write(str(array[i][j]) + "    ")
        f.write("\n")
    f.close
    a = [m,n]
    return a

def readFile1():
    array = np.loadtxt('./TH1_AI/array2.txt', dtype= int)
    return array

def WriteF2():
    print("Nhap so n:", end=" ")
    n = int(input())
    flag = 0
    array = []
    col = 0
    while flag < n:        
        array.append([])
        for j in range(0,10):
            if flag == n:
                break
            x = int(input("Nhap phan tu thu [%2d][%2d]: "%(col + 1, j+1)))
            array[col].append(x)
            flag+=1
        col+=1   

    f = open("./TH1_AI/array1.txt ","w")

    flag = 0
    col = 0
    while flag < n:        
        for j in range(0,10):
            if flag == n:
                break
            f.write(str(array[col][j]) + "    ")
            flag+=1
        col+=1
        f.write("\n")
    f.close
    a = n
    return a

def readFile2():
    array = []
    with open("./TH1_AI/array1.txt") as file:
        for item in file:
            item = item.split()
            array.append(item)            
    return array