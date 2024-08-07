"""
Source: Python for Data Analytics
Desc: Merging Operations in Pandas
All rights reserved Lotus Studios
7 Sep 22
"""

import pandas as pd
import numpy as np

# Merging Frames unexplicitly
frame1 = pd.DataFrame(

                        {
                            "id":['ball', 'pencil', 'pen', 'mug', 'ashtray'],
                            "price": [23,40,23,45,23]
                        }

                     )

# print(frame1)


frame2 = pd.DataFrame(

                        {
                            "id": ['pencil', 'pencil', 'ball', 'pen'],
                            "color": ['white','red','red','black']
                        }

                     )
# changing column name
# frame2.columns = ['ID', 'Brand Color']

# print(frame2)

# merge frame1 and frame2
merged_frame = pd.merge(frame1, frame2)
# print(merged_frame)


# Merging frames explicitly - using the on arguement
frame3 = pd.DataFrame(

                        {
                            "id":['ball', 'pencil', 'pen', 'mug', 'ashtray'],
                            "color": ['white','red','red','black', 'green'],
                            "brand": ['OMG', 'ABC', 'ABC', 'POD', 'POD']
                        }

                     )

# print(frame3)


frame4 = pd.DataFrame(

                        {
                            "id": ['pencil','pencil','ball','pen'],
                            "brand": ['OMG','POD','ABC','POD']
                        }

                     )

# print(frame4)


# merging explicitly
merged_ex_frame = pd.merge(frame3, frame4, on="id",)
print(merged_ex_frame)

