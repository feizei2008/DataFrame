# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 13:18:48 2017

@author: zack zhang
"""
import pandas as pd
import numpy as np
from pandas import DataFrame

tt=DataFrame(np.random.randn(7,6)) 
tt2 = tt.set_index(tt[tt.columns[0]])
print tt
print '--------------------'
print tt2
print '--------------------'
print tt2[tt2.columns[1]].tolist().index(tt2.iat[4,1])#1、把tt2第一列的series形式变成list；2、算该list中具体某个值的index
'''
因为tt2的index是随机数，实际上我们想获取的是index的值（这些随机数）
为什么上述操作没有把tt2.iat[4,1]的index的值获取，而只是获取了“4”呢？
因为对于list:[1.7029222470448384, -1.143576280285986, -1.335329729987041, 0.4573594040582438, -0.05128718711773473, 1.1057065973515106, -1.6397665748669927]
来说，其index只能是1,2,3,4,5这样
'''
