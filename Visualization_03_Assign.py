#Khoa Nguyen
#CS4650
#09-22-19
#Assignment_03_Visualization_graphs

#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read in data
grades = pd.read_csv('grades.csv')



#(1) a boxplot for weighted_total column.
plt.boxplot(grades['Weighted Total [Total Pts: up to 77.25 Percentage] |1258242'])
plt.show()



#(2) a multiple bar graph for 5 homework assignments for compare and contrast of students’ performance in these 5 assignments.
#grades.loc[2:13, 'Homework 2 [Total Pts: 20 Score] |1297002']
hwsort = grades[['Homework 1 [Total Pts: 20 Score] |1293619','Homework 2 [Total Pts: 20 Score] |1297002','Homework 3 [Total Pts: 20 Score] |1301007','Homework 4 [Total Pts: 20 Score] |1308148','Homework 5 [Total Pts: 20 Score] |1311965']]
hwsort.plot.bar()
plt.show()

#(3) a graph of your choice.
plt.style.use('seaborn')
excercise01 = grades['Exercise 1 [Total Pts: 5 Score] |1292496']
excercise02 = grades['Exercise 2 [Total Pts: 5 Score] |1293779']
excercise03 = grades['Exercise 3 [Total Pts: 5 Score] |1295703']
can = grades['Exercise 4 [Total Pts: 5 Score] |1298674']
plt.scatter(excercise01,excercise02,c=can, edgecolor='black',linewidth=2,alpha=0.75,cmap='summer')
cbar = plt.colorbar()
cbar.set_label('Excercise 1-3')
plt.title('Excercise 1-3 Scatter Plots',fontdict={'fontweight':'bold', 'fontsize': 13})
plt.tight_layout()
plt.savefig('Excercise 1-3 Scatter Plots.png', dpi=300)



#2. SP500 index stock data

#(1) a multiple-line graph (or other appropriate graph of your choice) to compare and contrast the performance Apple Inc. and Microsoft over a period of time provided in the data set. Use the stock close price.
#read in data
stocks = pd.read_csv('SP500_ind.csv')

#Microsoft Stocks sorted
microsoftStocks = stocks[ stocks['Symbol'] == 'MSFT' ]
#sort Apple stocks sorted
appleStocks = stocks[ stocks['Symbol'] == 'AAPL' ]

#Line Chart
plt.plot(appleStocks.Close, 'r.-', label="Apple Stocks")
plt.plot(microsoftStocks.Close, 'r.-', label="Apple Stocks")



#(2) an area plot graph (or other appropriate graph of your choice) to compare and contrast the trading volume of the above two companies.

#Area Graph
appleVol = appleStocks.Volume
microsoftVol = microsoftStocks.Volume


#(3)  a graph of your choice that compares at least three companies in certain way of your choice.
#plot line graph
#Adobe Stocks sorted
adobeStocks = stocks[ stocks['Symbol'] == 'ADBE' ]
#DirectTV Stocks sorted
directTVStocks = stocks[ stocks['Symbol'] == 'DTV' ]
plt.figure(figsize=(15,10))
plt.hist(appleStocks.High, color='#ffaf8c', edgecolor='black',label='Apple')
plt.hist(directTVStocks.High, color='#da8fa6', edgecolor='black',label='DirecTV',alpha=0.5)
plt.hist(adobeStocks.High, color='#70B793', edgecolor='black',label='Adobe',alpha=0.8)
plt.legend()
plt.title('Stock Histogram', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.xlabel('Stock Highs', fontdict={'fontweight':'bold', 'fontsize': 15})
plt.savefig('Stock Highs_Histogram.png', dpi=300)
plt.show()
