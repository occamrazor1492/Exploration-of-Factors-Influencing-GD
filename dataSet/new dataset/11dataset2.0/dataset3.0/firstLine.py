# -*- coding: utf-8 -*-

fileName = ["3.02.0co2 emissionsNew.csv","3.02.0commercial bank branchesNew.csv","3.02.0foreign direct investment net inflowsNew.csv","3.02.0internetUsersNew.csv","3.02.0labor forceNew.csv","3.02.0life expectancyNew.csv","3.02.0mobile cellular subscriptionsNew.csv","3.02.0technical articlesNew.csv","3.02.0time required to start a businessNew.csv","3.02.0unemployment rateNew.csv"]
## write name
#for i in fileName:
#    string1 = i[6:-7]
#    line = "Country Name, Year" + "," + string1
#    with open(i, 'r+') as f:
#        file_data = f.read()
#        f.seek(0,0)
#        f.write(line.rstrip('\r\n') + '\n' +file_data)
        
        
# combina all together
file1 = pd.read_csv("3.02.0GDP(constant 2010 US$)New.csv")





for i in fileName:
    file2 = pd.read_csv(i)
    file1 = pd.merge(file1, file2)

file1.to_csv("finalDataset.csv")
    
    