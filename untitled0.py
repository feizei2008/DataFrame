# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 13:18:48 2017

@author: zack zhang
"""
import pandas as pd
import numpy as np
from pandas import DataFrame
from numpy import nan as NA
Path = 'D:\\pythonLearn\\AShareCorrel\\'

#quotes = pd.read_csv(Path+'correl matrix.csv')

tt=DataFrame(np.random.randn(7,6)) 
tt2 = tt.set_index(tt[tt.columns[0]])
print tt
print '--------------------'
print tt2
print '--------------------'
#print tt[tt.columns[5]]
#print '--------------------'
#print tt.columns[2]
#print '--------------------'
print tt2[tt2.columns[1]].tolist().index(tt2.iat[4,1])#1、把tt2第一列的series形式变成list；2、算该list中具体某个值的index（而非该index的值）
#print list1
#print '==============================='
#print tt2.iat[4,1]
#print list1.index(tt2.ix[4,1])
#print len(quotes.index)
#print quotes.describe()
#print quotes.ix[:,3].count()
#print quotes.ix[1,:].count()
#print quotes.sum()
#
#
#
