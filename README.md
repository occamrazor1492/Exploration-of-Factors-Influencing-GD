# [CSCI_6906 Final Project](https://github.com/zhongziyun1993/DataVS_project)

## Website
**[Hosted on AWS, Link:](http://ec2-18-219-234-69.us-east-2.compute.amazonaws.com/)**


**[Report Link](https://dalu-my.sharepoint.com/:w:/g/personal/jn784780_dal_ca/ESsmL0MTzpZEsBTKajYXWM0B3ME90lLr6VY-JFEM5OK_Ug?e=bo9dwA)**

## Member
Ziyun Zhong, 

Fangye Tang, 

Yunfei Guo, 

Jingya Sun,<br>
Faculty of Computer Science
Dalhousie University
Halifax, Canada

## Topic
##### Exploration of Factors Influencing GDP
Abstract—GDP, Gross Domestics Products is a very abstract concept for non-economics professionals. For people to have a bettering understanding of GDP, we used machine learning, data classification, data regression on our pre-processed datasets. From the results, we found out which regressors are mostly contributed to GDP. Then, we used many different kinds of visualization modules to present our results. Users can interact with each visualization modules. From these modules, users get a good view about GDP.
Keywords—GDP, Machine learning, Regression, Visualization







## Download and Installation

To begin using this template, choose one of the following options to get started:
* Clone the repo: `git clone https://github.com/zhongziyun1993/DataVS_project`
* [Fork, Clone, or Download on GitHub](https:https://github.com/zhongziyun1993/DataVS_project)
* **$cd DataVS_project <br><h>$python -m SimpleHTTPServer**



## Project Structure
* index.html
* bundleChart.html -- bundleChart Relation between 4 selected regressor and other 6 unselected regressor
* resultChordChart.html -- How regressors relate to each other?
* resultPieChart -- How regressors contribute to GDP
* Jinya_6906_presentation -- K-mean classification result presentation
* dataSet
    * raw_data 
        * data_preprocessing.py  -- Choose year between 2004-2014, fill NaN with column average
        * data_preprocessingNew.py --  Choose year between 2004-2014, fill NaN with column average
        * *.csv -- raw csv file  
    * new dataset
        * *.csv -- csv file with year between 2004-2014 with out NaN value
        * fixColumnName.py -- fix the column name, delete irrelevant column
        * findInterMax.py -- do the combination of countries in each file, find the best option, delete unwanted countries in table
        * 11dataset2.0
            * *.csv -- regressors csv file that choose finally to do the machine learning, 141 countries, 11 tables including GDP
            * dataset3.0
                * *.csv -- formatted csv file ready to be integrated into one table 
                * firstLine.py -- integrated into one table
                * finalDatasetToby.csv -- final table


## Reference
* [World Bank Dataset](http://databank.worldbank.org/data/home.aspx)
* [NVD3](https://github.com/novus/nvd3)
* [D3 (or D3.js) JavaScript library](https://github.com/d3/d3)
* [scikit-learn Machine Learning in Python](http://scikit-learn.org/stable/index.html)
* [Bootstrap](https://github.com/twbs/bootstrap)
* [Nginx](https://www.nginx.com/resources/wiki/)
* [D3plus](https://d3plus.org/)
* [D3.json](http://learnjsdata.com/read_data.html)
* [jQuery](https://jquery.com/)
* [WEKA](https://www.cs.waikato.ac.nz/ml/weka/)
* [STATA14](https://www.stata.com/stata14/)
* [startbootstrap-landing-page](https://github.com/BlackrockDigital/startbootstrap-landing-page)


