import pandas as pd
import numpy as np
from collections import deque
import xlsxwriter

df1 = pd.read_excel("C:\\Users\ACER\OneDrive\Desktop\BUS.xlsx")
df2 = pd.read_excel("C:\\Users\ACER\OneDrive\Desktop\ict data.xlsx")
arr1 = np.array(df1.iloc[:, 0:1])
arr2 = np.array(df2.iloc[:, 0:1])
arr3 = np.array(df2.iloc[:, 2:3])

list1 = list()
for i in arr1:
    list1.append(int(i))
list2 = list()
for i in arr2:
    list2.append(int(i))
list3 = list()
for i in arr3:
    list3.append(int(i))

buffer = deque()
count = 1
for h in list1:
    n = h
    for i in list1:
        if n == i:
            buffer.append(i)
        else:
            pass
#### first search
    for i in list2:
        if buffer[0] == i:
            index = list2.index(i)
            buffer.append(list3[index])
        else:
            pass

    for j in list3:
        if buffer[0] == j:
            index = list3.index(j)
            buffer.append(list2[index])
        else:
            pass

#### second search
    for i in list2:
        if buffer[-1] == i:
            index = list2.index(i)
            buffer.append(list3[index])
        else:
            pass
    for j in list3:
        if buffer[-1] == j:
            index = list3.index(j)
            buffer.append(list2[index])
        else:
            pass

#### third search

    for i in list2:
        if buffer[-1] == i:
            index = list2.index(i)
            buffer.append(list3[index])
        else:
            pass
    for j in list3:
        if buffer[-1] == j:
            index = list3.index(j)
            buffer.append(list2[index])
        else:
            pass

    buffer_unique = set(buffer)
    temp = sorted(buffer_unique)
    length = len(temp)
    temp1 = []
    for i in range(length-1, -1, -1):
        #print(temp[i],end=" ")
        #print('-->',end=" ")
        temp1.append(temp[i])
    #print(temp1)
    writer = pd.ExcelWriter(r"C:\Users\ACER\OneDrive\Desktop\data.xlsx", engine="openpyxl")
    df3 = pd.DataFrame(temp1)
    df4 = df3.transpose()
    #print(df4)
    df4.to_excel(writer, startrow=count, startcol=1, index=False, header=False)
    count = count + 1
    buffer.clear()
    #print()
