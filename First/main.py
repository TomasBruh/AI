# Per senas tensorflow naudojamas šitam mokyme, net nebeduoda tokios atsisiųsti

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

# Load dataset.
df_train = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')  # training data
# csv-comma separated values
df_eval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')  # testing data
y_train = df_train.pop('survived')
y_eval = df_eval.pop('survived')

# print(df_train.head())  # prints 5 rows and some columns of the dataset
# print(df_train.describe())  # prints some more info about the dataset
# print(df_train.shape)  # prints out the shape of the dataset, this one has 627 entries with 9 features
# df_train.age.hist(bins=20)
# df_train.sex.value_counts().plot(kind='bar')
# plt.show()  # show the plot
