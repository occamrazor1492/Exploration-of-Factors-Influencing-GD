# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools
finalFileName = ["GDP(constant 2010 US$)New.csv","co2 emissionsNew.csv","commercial bank branchesNew.csv","foreign direct investment net inflowsNew.csv","internetUsersNew.csv","labor forceNew.csv","life expectancyNew.csv","mobile cellular subscriptionsNew.csv","technical articlesNew.csv","time required to start a businessNew.csv","unemployment rateNew.csv"]
finalFile11 = ["2.0GDP(constant 2010 US$)New.csv","2.0co2 emissionsNew.csv","2.0commercial bank branchesNew.csv","2.0foreign direct investment net inflowsNew.csv","2.0internetUsersNew.csv","2.0labor forceNew.csv","2.0life expectancyNew.csv","2.0mobile cellular subscriptionsNew.csv","2.0technical articlesNew.csv","2.0time required to start a businessNew.csv","2.0unemployment rateNew.csv"]


print(len(finalFileName))

# find the intersection
def findIntersection(fileName):
    countryNameList = []
    country = []
    for i in fileName:
        country = []
        file = pd.read_csv(i)
        for j in range(0, file.shape[0]):
            countryName = file.iloc[j,0]
            
            country.append(countryName)
        countryNameList.append(set(country))
    u = set.intersection(*countryNameList)
    return u


u = findIntersection(finalFileName)
    
    


co2 = pd.read_csv("co2 emissionsNew.csv")
constant = co2.shape[0]


for c in range(0, constant):
    name = co2.iloc[c, 0]
    print(name)
    if name not in u:
        co2.iloc[c, 4] = np.NaN

co2 = co2.dropna(axis = 0, how = 'any')
co2 = co2.reset_index()
co2 = co2.drop(co2.columns[0], axis = 1)
#for i in range(0,3):
#    co2 = co2.drop(co2.columns[1], axis = 1)
co2.set_index('Country Name', inplace=True)
co2 = co2.drop('Country Code', axis= 1)
co2 = co2.drop('Series Name', axis= 1)
co2 = co2.drop('Series Code', axis= 1)


# set colums index
co2.columns = [i for i in range(2004, co2.shape[1]+2004)]






stacked = co2.stack()


stacked.to_csv("test.csv")

test = pd.read_csv("test.csv")

test.columns = ['Country Name', 'Year', 'Co2']






for k in finalFileName:
    file = pd.read_csv(k)
    row = file.shape[0]
    for d in range(0, row):
        countryName = file.iloc[d, 0]
        if countryName not in u:
            file.iloc[d, 4] = np.NaN
    file = file.dropna(axis = 0, how = 'any')
    file = file.reset_index()
    file = file.drop(file.columns[0], axis = 1)
    
    file.to_csv("11dataset2.0/"+"2.0"+k)

# test if the new 11 file is correct
for s in finalFile11:
    file2 = pd.read_csv("11dataset2.0/"+s)
    row2 = file2.shape[0]
    print(row2)
    