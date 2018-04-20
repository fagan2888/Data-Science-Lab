
"""
Created on Fri Apr 20 15:38:55 2018

@author: Nodar.Okroshiashvili

"""


# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%


# Importing the dataset

dataset = pd.read_csv('data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#%%

# Dealing with missing data

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

"""
Here missing value are denoted as NaN, and we use sample mean to extrapolate missing observation

"""

#%%


# Encoding categorical data
# Encoding the Independent Variable

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

"""
We see here that we have three categories in country column.
Since machine learning algorithms only "sees" the numbers and we have 0, 1, and 2,
then this algorithm thinks that 1 is preferred than 0, and 2 is preferred than 1
So, algorithm will give more weight to 2 and will have kind of bias towards Germany or 2.
We need to create dummy variable. Since we have three categories we need three dummy variables.
But, among these three we have to discard one, to avoid dummy variable trap.

"""
# Changes text into numbers in country column
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

# Creates dummy variables for country
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()


# Encoding the Dependent Variable
# Dependent variable is binary yes/no and labelencoder converts it to numeric value

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#%%

# Split dataset into Training set and Test set
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#%%


# Feature scaling

"""
In Machine Learning algorithms, scale of variable is too important.
If one variable scale is higher than the other's
then the algorithm based on Euclidean distance will give more weight first variable then second.
So, we absolutely need to put these two variables in the same scale.

Feature Scaling is a must for algorithms which uses Euclidean or other notion of distances.


For the training set use Fit and Transform, whereas for the test set use only Transform method.


"""
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()

X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)

#%%



"""

Please, note that the complexity of preprocessing and steps to do
in this level is directly proportional to the how messy the data set is.
Generally, 80% of effort is needed to clean the data and 20% in enough to build the model

"""
