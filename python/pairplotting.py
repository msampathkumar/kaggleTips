'''
How to create a pairplot(R) in Python?

Source: http://stackoverflow.com/questions/2682144/matplotlib-analog-of-rs-pairs
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.DataFrame(np.random.randn(1000, 4), columns=['A','B','C','D'])
axes = pd.tools.plotting.scatter_matrix(df, alpha=0.2)
plt.tight_layout()
plt.savefig('scatter_matrix.png')
