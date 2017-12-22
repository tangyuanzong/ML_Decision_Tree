#!/usr/bin/python
#coding=utf-8
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.animation as ai
import numpy as np
import math


def splitData(data, axis, value):               #数据分割
    retdata = []                                #包含value的数据
    splitdata = []                              #不包含value的数据
    for fat in data:
        reducefat = fat[:axis]
        reducefat.extend(fat[axis + 1:])
        if fat[axis] == value:
           retdata.append(reducefat)
        else:
           splitdata.append(reducefat)
    return retdata
           

def shannon_data(data):                       #经验熵
    number = len(data)
    labelcount = {}
    for d in data:
        label = d[-1]
        if label not in labelcount.keys():
          labelcount[label] = 0
        labelcount[label] += 1
    shannon = 0.0
    for key in labelcount:
        p = float(labelcount[key]) / number
        shannon -= p * math.log(p, 2)          #H(pi) = p * log(p, 2)
    return shannon

def shannon_conditional(data, i, feat, unique):  #条件熵
    ce =0.0
    for value in unique:
        subdata = splitData(data, i , value)
        p = len(subdata) / float(len(data))
        ce +=p * shannon_data(subdata)
    return ce

def Infor_Gain(data, base, i):          #计算信息增益
    featList = [example[i] for example in data]  # 第i维特征列表
    uniqueVals = set(featList)                   # 转换成集合
    newEntropy = shannon_conditional(data, i, featList, uniqueVals)
    infoGain = base - newEntropy                 # 信息增益，就是熵的减少，也就是不确定性的减少
    return infoGain

def Infor_GainRate(data, base, i): #计算信息增益比
    return Infor_Gain(data, base, i) / base


def C4_5(data):
    numFeatures = len(data[0]) - 1  # 最后一列是分类
    baseEntropy = shannon_data(data)
    bestInfoGainRate = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 遍历所有维度特征
        infoGainRate = Infor_GainRate(data, baseEntropy, i)
        if (infoGainRate > bestInfoGainRate):  # 选择最大的信息增益
            bestInfoGainRate = infoGainRate
            bestFeature = i
    return bestFeature  # 返回最佳特征对应的维度

