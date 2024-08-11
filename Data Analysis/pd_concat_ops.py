"""
Source: Python for Data Analytics
Desc: Concatenating Operations in Pandas
All rights reserved Akintola Technologies 7 Sep 22 updt Aug 24
"""
import numpy as np
import pandas as pd

# explicit numpy array creation
arr1 = np.array([
                    [0,1,2],
                    [3,4,5],
                    [6,7,8]
                ])

# implicit numpy array creation
arr2 = np.arange(9).reshape((3,3))+6
# print(arr2)

concat = np.concatenate([arr1,arr2], axis=1)
# print(concat)

# implicit creation of a series DataFrame
ser1 = pd.Series(np.random.rand(4), index=[1,2,3,4])
ser2 = pd.Series(np.random.rand(4), index=[5,6,7,8])
# print(ser2)

# concat series DataFrame
ser_concat = pd.concat([ser1,ser2], axis=1)
print(ser_concat)
