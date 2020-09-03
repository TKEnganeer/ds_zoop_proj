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
df['prop_price_k'] = df['price'].div(1000)

# choose relevant columns
# 'closest_station'
df.columns
# simplified price column to thousands so graphs read better

df_model = df [[ 'prop_price_k', 'title', 'closest_st_miles', 'prop_pc',
        'd_from_c', 'listed_on_2', 'location_simp', 'description_simp',
        'gard_feat_yn', 'large_feat_yn', 'spacious_feat_yn',
        'extension_feat_yn']]
# get dummy data
df_dum = pd.get_dummies(df_model)

# train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('prop_price_k', axis = 1)
y = df_dum.prop_price_k.values

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
lm_l.fit(X_train, y_train)
np.mean(cross_val_score(lm_l,X_train,y_train, scoring= 'neg_mean_absolute_error', cv = 3))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha = (i/100))
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
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion': ('mse', 'mae'), 'max_features':('auto', 'sqrt', 'log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error', cv = 3)
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_
# test ensembles 
tpred_lm = lm.predict(X_test)
tpred_lm_l = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lm_l)
mean_absolute_error(y_test, tpred_rf) 

mean_absolute_error(y_test, (tpred_lm_l+tpred_rf)/2) 
# combining models
import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open('model_file' +'.p','wb'))

file_name = 'model_file.p'
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
    
model.predict(X_test.iloc[1,:].values.reshape(1,-2))





