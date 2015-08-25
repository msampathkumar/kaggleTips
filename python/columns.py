'''
Here are few generic way you can apply to convert - few object columns to int64
'''
import numpy as np
import pandas as pd

from sklearn import preprocessing

for i in range(df_train.shape[1]):
    lbl_enc = preprocessing.LabelEncoder()
    if df_train[df_train.columns[i]].dtype != 'int64':
      # converting to int64
      df_train[df_train.columns[i]] = lbl_enc.fit_transform(df_train[df_train.columns[i]])
