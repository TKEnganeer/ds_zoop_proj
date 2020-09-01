# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:56:12 2020

@author: TimK
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/TimK/Documents/ds_zoop_proj/zeda_data.csv")
df = df.dropna()

# choose relevant columns
# 'closest_station'
df.columns

df_model = df [[ 'price', 'title', 'closest_st_miles', 'prop_pc',
        'd_from_c', 'listed_on_2', 'location_simp', 'description_simp',
        'gard_feat_yn', 'large_feat_yn', 'spacious_feat_yn',
        'extension_feat_yn']]
# get dummy data
df_dum = pd.get_dummies(df_model)

# train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('price', axis = 1)
y = df_dum.price.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# multiple linear regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)

model.fit().summary()

# sm.show_versions()
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring= 'neg_mean_absolute_error', cv = 3))


# lasso regression
lm_l = Lasso()
np.mean(cross_val_score(lm_l,X_train,y_train, scoring= 'neg_mean_absolute_error', cv = 3))

alpha = []
error = []

for i in range(1,5000):
    alpha.append(i/10)
    lml = Lasso(alpha = (i/10))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring= 'neg_mean_absolute_error', cv = 3)))
    
plt.plot(alpha,error)

err = tuple(zip(alpha, error))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)]

# random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf, X_train, y_train, scoring= 'neg_mean_absolute_error', cv = 3))
# support vector regression (optional)
# tune models GridsearchCV
# test ensembles 


