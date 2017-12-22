#!/usr/bin/python
#coding=utf-8
import xlrd

def read_xls_file():                            #读取excel文件
    data = xlrd.open_workbook('./ex3data.xls')  #打开文件
    sheet1 = data.sheet_by_index(0)             #获取sheet
    m = sheet1.nrows                            #获取行大小
    n = sheet1.ncols                            #获取列大小
    dataMat = []                         
    label = []                                  #标签
    for i in range(m):                          #枚举每一行
        row_data = sheet1.row_values(i)         #获取一行数据
        del(row_data[0])                        #删除第一列
        if(i == 0):                             #标签
           label = row_data                     #获取标签 
        elif(i > 0 ):                           #其他数据      
           dataMat.append(row_data)
    return dataMat,label
