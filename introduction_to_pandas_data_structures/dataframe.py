# -*- coding: utf-8 -*-
import numpy as np
from pandas import Series, DataFrame

print '用字典生成DataFrame，key为列的名字。'
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
print DataFrame(data)
print DataFrame(data, columns = ['year', 'state', 'pop']) # 指定列顺序
print

print '指定索引，在列中指定不存在的列，默认数据用NaN。'
frame2 = DataFrame(data,
                    columns = ['year', 'state', 'pop', 'debt'],
                    index = ['one', 'two', 'three', 'four', 'five'])
print frame2
print frame2['state']
print frame2.year
print frame2.ix['three']
frame2['debt'] = 16.5 # 修改一整列
print frame2
frame2.debt = np.arange(5)  # 用numpy数组修改元素
print frame2
print


