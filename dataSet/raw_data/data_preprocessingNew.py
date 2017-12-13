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
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(E[:, 0:columsE])
#E[:, 0:columsE] = imputer.transform(E[:, 0:columsE])
#expect.to_csv("commercial bank branchesNew.csv")

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

#--------------------   New ----------------

new = pd.read_csv("co2 emissions.csv")





