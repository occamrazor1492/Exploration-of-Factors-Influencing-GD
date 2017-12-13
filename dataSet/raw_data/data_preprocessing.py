# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#dataset = pd.read_csv('Life expectancy at birth, total (years).csv')
#print(dataset.shape)
##X = dataset.iloc[:, :61].values
##print(X.shape)
#b = dataset.iloc[:, :1]
#
##df = df.dropna()
##print(df.shape)
#
##df1 = df[df['1960 [YR1960]'] != '..']
##print(df1.shape)
#
## drop the last column
#df = dataset.drop('2016 [YR2016]', axis= 1)
#print(df.shape)
#
#
#df1 = df[df.iloc[:, :60] != '..']
#df1 = df1.dropna(axis = 0, how = 'any')
#print(df1.shape)
#b = df1.iloc[:, :1]

## co2----------------------------------------
#df2 = pd.read_csv('CO2_emissions(kt).csv')
#
#
#
#df2 = df2[df2.iloc[:, :61] != '..']
#
#df2 = df2.dropna(axis=1, how='all')
#
#df2 = df2.dropna(axis = 0, how = 'any')
#
#
#c = df2.iloc[:,:1]
#
#frams = pd.concat([b,c], axis = 1)
#frams = frams.dropna(axis = 0, how = 'any')
#print(frams.shape)

# -------------firms using banks to finance investment.csv
firm = pd.read_csv('commercial bank branches.csv')
print(firm.shape)

firm = firm[firm.iloc[:,:31] != '..']
firm = firm.dropna(axis = 1, how = 'all')
print(firm.shape)
firm = firm.drop('2001 [YR2001]', axis= 1)
firm = firm.drop('2002 [YR2002]', axis= 1)
firm = firm.drop('2003 [YR2003]', axis= 1)


firm = firm.dropna(subset=['2014 [YR2014]', '2015 [YR2015]'], how='all')
colums = firm.shape[1]
#inflow.to_csv("foreign direct investment net inflowsNew.csv")
#X = firm.iloc[:, 4:colums].values
## replace NaN with mean
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(X[:, 0:colums])
#X[:, 0:colums] = imputer.transform(X[:, 0:colums])
#inflow.to_csv("foreign direct investment net inflowsNew2.csv")

# ------------- foreign direct investment net inflows.csv
inflow = pd.read_csv('foreign direct investment net inflows.csv')
colums = inflow.shape[1]
inflow = inflow[inflow.iloc[:,:colums] != '..']
inflow = inflow.drop('2016 [YR2016]', axis= 1)
inflow = inflow.dropna(axis = 1, how = 'all')
inflow = inflow.dropna(subset=['1993 [YR1993]', '1994 [YR1994]'], thresh=1)
inflow = inflow.dropna(subset=['1991 [YR1991]', '1992 [YR1992]'], how='all')
inflow = inflow.dropna(subset=['2014 [YR2014]', '2015 [YR2015]'], how='all')
colums = inflow.shape[1]
#inflow.to_csv("foreign direct investment net inflowsNew.csv")
X = inflow.iloc[:, 4:colums].values
# replace NaN with mean
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 0:colums])
X[:, 0:colums] = imputer.transform(X[:, 0:colums])
inflow.to_csv("foreign direct investment net inflowsNew2.csv")

# ------------ life expectancy.csv ------------
expect = pd.read_csv("life expectancy.csv")
columsE = expect.shape[1]
# convert to NaN
expect = expect[expect.iloc[:,:columsE] != '..']
# drop All 'every cell is NaN' colums 
expect = expect.dropna(axis = 1, how = 'all')
# ..... row
expect = expect.dropna(axis = 0, how = 'all')

expect = expect.dropna(subset=['1993 [YR1993]', '1994 [YR1994]'], thresh=1)
expect = expect.dropna(subset=['1991 [YR1991]', '1992 [YR1992]'], how='all')
expect = expect.dropna(subset=['2014 [YR2014]', '2015 [YR2015]'], how='all')
columsE = expect.shape[1]

E = expect.iloc[:, 4:columsE].values
# replace NaN with mean
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(E[:, 0:columsE])
E[:, 0:columsE] = imputer.transform(E[:, 0:columsE])
expect.to_csv("life expectancyNew.csv")










