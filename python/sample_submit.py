# kaggle # titanic

# sample submission file

import numpy as np
import pandas as pd

from sklearn.ensemble import GradientBoostingClassifier
from sklearn import preprocessing
from sklearn.cross_validation import cross_val_score

#Print you can execute arbitrary python code
df_train = pd.read_csv("../input/train.csv", dtype={"Age": np.float64}, )
df_test = pd.read_csv("../input/test.csv", dtype={"Age": np.float64}, )

# Drop NaNs
df_train.dropna(subset=['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'], inplace=True)

# Lucky names
df_train['Name'] = df_train['Name'].str.extract('(Mr\. |Miss\. |Master. |Mrs\.[A-Za-z ]*\()([A-Za-z]*)')[1]
df_test['Name'] = df_test['Name'].str.extract('(Mr\. |Miss\. |Master. |Mrs\.[A-Za-z ]*\()([A-Za-z]*)')[1]

# names to hash
df_test['Name'] = df_test['Name'].map(hash)
df_train['Name'] = df_train['Name'].map(hash)

# names to hash
df_test['Cabin'] = df_test['Cabin'].fillna(value='None')
df_train['Cabin'] = df_train['Cabin'].fillna(value='None')


for i in range(df_train.shape[1]):
    lbl_enc = preprocessing.LabelEncoder()
    if df_train[df_train.columns[i]].dtype != 'int64':
        df_train[df_train.columns[i]] = lbl_enc.fit_transform(df_train[df_train.columns[i]])


for i in range(df_test.shape[1]):
    lbl_enc = preprocessing.LabelEncoder()
    if df_test[df_test.columns[i]].dtype != 'int64':
        df_test[df_test.columns[i]] = lbl_enc.fit_transform(df_test[df_test.columns[i]])


selected_columns = ['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

########################  Training data

X = df_train[selected_columns]
y = df_train['Survived']

clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=2, random_state=0).fit(X, y) # trained model


########################  Applying trained model on test data

X = df_test[selected_columns]
y = clf.predict(X)

submission = pd.DataFrame({ 'PassengerId': df_test['PassengerId'], 'Survived': y })
submission.to_csv("submission.csv", index=False)

