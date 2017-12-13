import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ---- commercial bank branches----------
#expect = pd.read_csv("commercial bank branches.csv")
#columsE = expect.shape[1]
## convert to NaN
#expect = expect[expect.iloc[:,:columsE] != '..']
## drop All 'every cell is NaN' colums
#expect = expect.dropna(axis = 1, how = 'all')
## ..... row
#expect = expect.dropna(axis = 0, how = 'all')
#
#expect = expect.drop('2001 [YR2001]', axis= 1)
#expect = expect.drop('2002 [YR2002]', axis= 1)
#expect = expect.drop('2003 [YR2003]', axis= 1)
#
##expect = expect.dropna(subset=['2001 [YR2001]', '2002 [YR2002]'], thresh=1)
#expect = expect.dropna(subset=['2004 [YR2004]', '2005 [YR2005]'], how='all')
#expect = expect.dropna(subset=['2014 [YR2014]', '2015 [YR2015]'], how='all')
#columsE = expect.shape[1]
#
#E = expect.iloc[:, 4:columsE].values
## replace NaN with mean
# from sklearn.preprocessing import Imputer
# imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# imputer = imputer.fit(E[:, 0:columsE])
# E[:, 0:columsE] = imputer.transform(E[:, 0:columsE])
# expect.to_csv("commercial bank branchesNew.csv")

# ----- Gini index ---------
#expect = pd.read_csv("gini index.csv")
#columsE = expect.shape[1]
## convert to NaN
#expect = expect[expect.iloc[:,:columsE] != '..']
## drop All 'every cell is NaN' colums
#expect = expect.dropna(axis = 1, how = 'all')
## ..... row
#expect = expect.dropna(axis = 0, how = 'all')
## delete colum by index
#
#b = []
#for i in range(4, 18):
#    b.append(i)
#
#expect = expect.drop(expect.columns[b],axis = 1)
#
#
##expect = expect.dropna(subset=['2001 [YR2001]', '2002 [YR2002]'], thresh=1)
#expect = expect.dropna(subset=['2004 [YR2004]', '2005 [YR2005]'], how='all')
#expect = expect.dropna(subset=['2014 [YR2014]', '2015 [YR2015]'], how='all')
#columsE = expect.shape[1]
#
#E = expect.iloc[:, 4:columsE].values
## replace NaN with mean
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(E[:, 0:columsE])
#E[:, 0:columsE] = imputer.transform(E[:, 0:columsE])
#expect.to_csv("gini indexNew.csv")



# ------------- internet users.csv ------------
#expect = pd.read_csv("co2 emissions.csv")
#columsE = expect.shape[1]
#
## convert to NaN
#expect = expect[expect.iloc[:,:columsE] != '..']
## drop All 'every cell is NaN' colums
#expect = expect.dropna(axis = 1, how = 'all')
## ..... row
#expect = expect.dropna(axis = 0, how = 'all')
## delete colum by index
#
#b = []
#for i in range(4, 17):
#    b.append(i)
#
#expect = expect.drop(expect.columns[b],axis = 1)
##expect = expect.dropna(subset=['2005 [YR2005]', '2006 [YR2006]'], thresh=1)
#expect = expect.dropna(subset=['2004 [YR2004]', '2005 [YR2005]'], how='all')
#expect = expect.dropna(subset=['2012 [YR2012]', '2013 [YR2013]'], how='all')
#columsE = expect.shape[1]
#E = expect.iloc[:, 4:columsE].values
## replace NaN with mean
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(E[:, 0:columsE])
#E[:, 0:columsE] = imputer.transform(E[:, 0:columsE])
#expect.to_csv("co2 emissionsNew.csv")
# 0-------------
# ------------------------   Country Name ----------------
constantFileName = fileName


fileName = constantFileName
fileName = ["GDP(constant 2010 US$)New.csv","co2 emissionsNew.csv","commercial bank branchesNew.csv","foreign direct investment net inflowsNew.csv","gini indexNew.csv","government expenditure on educationNew.csv","internetUsersNew.csv","labor forceNew.csv","life expectancyNew.csv","mobile cellular subscriptionsNew.csv","railways goods transportedNew.csv","school life expectancyNew.csv","technical articlesNew.csv","time required to start a businessNew.csv","unemployment rateNew.csv"]
country = []




# see the index and row number
tempIndex = 0
# find the min country list
for m in fileName:

    fileM = pd.read_csv(m)
    print(str(tempIndex) + "    "+str(fileM.shape[0]) + "      "+m + "    ")
    tempIndex += 1


# see what is the intersecition after delete one of the file
def cal(fileName, index):
    delName = fileName[index]
    fileName.pop(index)
    #print(fileName[index])7
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
    print(str(len(u)) + "  " + delName)

for i in range(0, len(constantFileName)):
    fileName = ["GDP(constant 2010 US$)New.csv","co2 emissionsNew.csv","commercial bank branchesNew.csv","foreign direct investment net inflowsNew.csv","gini indexNew.csv","government expenditure on educationNew.csv","internetUsersNew.csv","labor forceNew.csv","life expectancyNew.csv","mobile cellular subscriptionsNew.csv","railways goods transportedNew.csv","school life expectancyNew.csv","technical articlesNew.csv","time required to start a businessNew.csv","unemployment rateNew.csv"]

    cal(fileName, i)






# find intersectiona
countryNameList = []
country = []
for i in fileName:
   country = []
   file = pd.read_csv(i)
   for j in range(0, file.shape[0]):
       countryName = file.iloc[j,0]


       country.append(countryName)
#   country = list(set(country))
   countryNameList.append(set(country))

for items in countryNameList:
    print(len(items))



intersection= list(set.intersection(*map(set, countryNameList)))
u = set.intersection(*countryNameList)
print(len(u))




print(country)

# final data set operation
for a in fileName:
    file = pd.read_csv(a)
    for b in range(0,file.shape[0]):
        countryName2 = file.iloc[,0]
        if countryName2 not in country:
            file.drop(file.index[i], inplace = True)


#    for j in range()
#    countrySet = Set()
co2 = pd.read_csv("co2 emissionsNew.csv")
co22 = pd.read_csv("co2 emissionsNew.csv")
constant = co2.shape[0]

for c in range(0, constant):
    name = co2.iloc[c, 0]
    print(name)
    if name not in intersection:

        co2 = co2.drop(co2.index[c], inplace = True)


#--------------------   New ----------------


branch = pd.read_csv("commercial bank branchesNew.csv").drop('2015 [YR2015]', axis= 1)
dataset = pd.read_csv("final dataset.csv")

# new col
dataset['commercial bank branches'] = np.NaN

col = branch.shape[1]
row= branch.shape[0]
rowNumDataset = 0

#dataset.iloc[0,3] = 1234
# use ls > filename.txt and then use regx








for rowNumBranch in range(0, row):
    for j in range(5, 16):
        if dataset.iloc[rowNumDataset,0] == branch.iloc[rowNumBranch,1]:
            dataset.iloc[rowNumDataset,3] = branch.iloc[rowNumBranch, j]


        else:
            print("error")
            print("---------------rowNumBranch:     " + str(rowNumBranch) + "    rowNumDataset:    " + str(rowNumDataset) + "    ---     " + str(j) )

        rowNumDataset += 1

dataset.dropna(axis = 0, how = 'any')
