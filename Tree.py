#!/usr/bin/python
#coding=utf-8

from pylab import *
import matplotlib.pyplot as plt
from readfile import *
from ID3 import *
from c4_5 import *
from create_tree import *

def classify(inputTree,featLabels,testVec):  #根据已有的决策树，对给出的数据进行分类
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)  #这里是将标签字符串转换成索引数字
    for key in secondDict.keys():
        if testVec[featIndex] == key:       #如果key值等于给定的标签时
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key],featLabels,testVec) #递归调用分类
                #print classLabel
            else: classLabel = secondDict[key] #此数据的分类结果

    return classLabel

def storeTree(inputTree, filename): #储存决策树
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename): #读取决策树
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)
	
	
def pred(data,myTree,labelcopy): #预测函数
    m, n =shape(data)
    sum1 = 0
    for i in range(m):
        s = classify(myTree,labelcopy,data[i])
        if (s == data[i][3]):
           sum1 +=1
    print "正确率" , float(sum1)/float(m)

data, labels = read_xls_file()
labelcopy = []
m = len(labels)
for i in range(m):
    labelcopy.append(labels[i])


myTree = createTree(data, labels)
pred(data,myTree,labelcopy)
createPlot(myTree)

