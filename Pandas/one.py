# Selecting data from a dataframe using conditions/conditional selecting

import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)

# Create a dataframe with the above seed
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())

df[df>0] # Select data that meets this condition. Returns a boolean.

df[df['W']>0] # Returns a row(s) that satisfies this condition.

# Adding more soup: going deeper to just get a series after the previous
# step:
df[df['W']>0]['Y'] # Select values of "Y" that comes from the previous satisfactions

# Even more soup:
df[df['W']>0][['Y','X']]

# For multiple conditional selecting:
df[(df['W']>0) & (df['Y'] > 1)] # Keep in mind that we need not to use pythons's "and" nor "or".

"""
    Multi-Index and index hierarchy
"""

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])

"""
Output Structure:

                A	        B
    G1	1	0.153661	0.167638
        2	-0.765930	0.962299
        3	0.902826	-0.537909
    G2	1	-1.549671	0.435253
        2	1.259904	-0.447898
        3	0.266207	0.412580
"""

# Index crossectioning
df.xs('G1')

df.xs(1,level='Num')
"""
Returns:
            A	        B
Group		
G1	    0.153661	0.167638
G2	    -1.549671	0.435253
"""