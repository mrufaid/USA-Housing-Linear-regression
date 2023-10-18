# -*- coding: utf-8 -*-
"""Linear_regresson_Pr1_p1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10rqO6TMduVmF_i_83Ub6rSu1uC4fXr4c

The dataset was imported from the link 'https://www.kaggle.com/datasets/kanths028/usa-housing/ '.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#read the csv file
df=pd.read_csv('/content/drive/MyDrive/USA_Housing.csv')

#printing and checking if csv file is read properly
print(df.head())
print(df.keys())

#plotting graphs between variables in the dataframe
sns.pairplot(df)

#plotting correlation matrix to check correlation of variables with the price

correlation_matrix=df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

#preparing data for training after examining correlation between variables
#skipping variables with poor corelation
x=df[['Area Population','Avg. Area Number of Rooms','Avg. Area House Age','Avg. Area Income']]
y=df['Price']

#splitting data into train and test dataset

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=43)

#creating instance of Linear regression function
lr=LinearRegression()
lr.fit(x_train,y_train)  #Training model

#printing intercept and coeeficient of the linear regression line
print(lr.intercept_)
print(lr.coef_)

#test the model to predict the points in x_test dataset
prediction = lr.predict(x_test)

#compare the predictions with the actual data
sns.scatterplot(x=prediction, y=y_test)
plt.xlabel('prediction')
plt.ylabel('actual value')

df1=pd.DataFrame(prediction,y_test)

sns.distplot((y_test - prediction))

metrics.mean_absolute_error(y_test, prediction)

metrics.mean_squared_error(y_test, prediction)

np.sqrt(metrics.mean_squared_error(y_test, prediction))

