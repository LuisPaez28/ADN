from sklearn.datasets import load_boston
boston_dataset = 

description = boston_dataset.DESCR

print(description[148:1225])

import pandas as pd 
df = pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
df.head()

df['MEDV'] = boston_dataset.target[df.index]

df.head()

df.shape

df.describe()

import seaborn as sns
import matplotlib.pyplot as plt
