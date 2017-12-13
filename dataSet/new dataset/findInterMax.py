#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:28:57 2017

@author: ziyunzhong
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools

fileName = ["GDP(constant 2010 US$)New.csv","co2 emissionsNew.csv","commercial bank branchesNew.csv","foreign direct investment net inflowsNew.csv","gini indexNew.csv","government expenditure on educationNew.csv","internetUsersNew.csv","labor forceNew.csv","life expectancyNew.csv","mobile cellular subscriptionsNew.csv","railways goods transportedNew.csv","school life expectancyNew.csv","technical articlesNew.csv","time required to start a businessNew.csv","unemployment rateNew.csv"]


        
def CountryNameList(fileName):
    countryNameList = []
    country = []
    for i in fileName:
        country = []
        file = pd.read_csv(i)
        for j in range(0, file.shape[0]):
            countryName = file.iloc[j,0]
            
            country.append(countryName)
        countryNameList.append(set(country))
        
    return countryNameList

def findInter(fileName, select):
    countryNameList = CountryNameList(fileName)
    selectedList = list(itertools.combinations(countryNameList,select))
    for i in range(0, len(selectedList)):
        selectedList[i] = list(selectedList[i])
    uList = []
    for item in selectedList:
        u = set.intersection(*item)
        number = len(u)
        
        uList.append(number)
    return max(uList)

#for i in range(5, 16):
#    print(i)
#    print(findInter(fileName, i))
#    print("-----------------")