# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools



finalFile11 = ["2.0GDP(constant 2010 US$)New.csv","2.0co2 emissionsNew.csv","2.0commercial bank branchesNew.csv","2.0foreign direct investment net inflowsNew.csv","2.0internetUsersNew.csv","2.0labor forceNew.csv","2.0life expectancyNew.csv","2.0mobile cellular subscriptionsNew.csv","2.0technical articlesNew.csv","2.0time required to start a businessNew.csv","2.0unemployment rateNew.csv"]


for items in finalFile11:
    co2 = pd.read_csv(items)

    constant = co2.shape[0]
    co2 = co2.drop(co2.columns[0], axis = 1)
    co2.set_index('Country Name', inplace=True)
    co2 = co2.drop('Country Code', axis= 1)
    co2 = co2.drop('Series Name', axis= 1)
    co2 = co2.drop('Series Code', axis= 1)
    co2.columns = [i for i in range(2004, co2.shape[1]+2004)]

    stacked = co2.stack()
    stacked.to_csv("dataset3.0/"+"3.0"+items)
    
    
    
    
    
# ---------- 1 example-----------
#co2 = pd.read_csv("2.0co2 emissionsNew.csv")
#constant = co2.shape[0]
#co2 = co2.drop(co2.columns[0], axis = 1)
#co2.set_index('Country Name', inplace=True)
#co2 = co2.drop('Country Code', axis= 1)
#co2 = co2.drop('Series Name', axis= 1)
#co2 = co2.drop('Series Code', axis= 1)
#co2.columns = [i for i in range(2004, co2.shape[1]+2004)]
#
#stacked = co2.stack()
#stacked.to_csv("test.csv")





