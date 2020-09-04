# Data Science Outer London House Price Estimator: Project Overview
* Created a tool to estimate the house prices for properties < 40 miles from central London less than £325k (MAE ~ £19K) to help people when looking for homes at commutable distance. 
* I scraped over 900 property descriptions from zoopla.co.uk using python and beautifulsoups.
* Engineered features from the text for each decsription to quantify how the value of house prices change if are description were to have a garden, largeness, spaciousness or an extention featured in the description.
* Optimised Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

## Code and Resources Used
**Python Version:** 3.8

**Packages:** pandas, numpy, sklearn, matplotlib, seasborn, beautifulsoups, flask, json, pickle.

**For Web Framework Requirements:** pip install -r requirements.txt

**Data Science Project Tutorial Series:** https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

**Scraper Tutorial:** https://www.youtube.com/watch?v=Itqfkgw508U

**Postal code geocoding and distance calculation Github:** https://github.com/rth/pgeocode

**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping
I adapated the web scraper from the youtube video (above) to suit my search creteria - *"A 3 bedroom house at a maximum 40 miles radius from central London under £325k."*. I used this information to scrape about 900 property information postings on zoopla.co.uk. I got the following information from each property:
* title 
* address 
* description 
* price 
* estate agent phone number
* closest_station (to property)
* listed_on (date listed) 
* image link (of property)
* closest_st_miles (distance to closest train station)
* prop_pc (postcode) 

## Data Cleaning

After scraping the data, I cleaned so it could be more usable in my model. I made further changes and created the following variables: 
* Parsed numeric data from property price and simplified it
* Property distance from central London (W2 2SZ) 
* Numerical value for date listed 
* Columns for simplified location and description information:
  * grouped the adresses into regions - Luton, Essex, Kent etc.
  * Isolated the key property features from the description and grouped them  
* Made columns for the following property features found in the description:
  * garden 
  * large 
  * spacious 
  * extension 
* Column for decscription length

## EDA

I looked at the distributions of the data and the value counts for the various categorical variables. Below some highlights from my pivot tables.

![alt text](https://github.com/TKEnganeer/ds_zoop_proj/blob/master/hp_correlation_visual.PNG "Correlations")
![alt text](https://github.com/TKEnganeer/ds_zoop_proj/blob/master/price_by_location.PNG "Price by Location")
![alt text](https://github.com/TKEnganeer/ds_zoop_proj/blob/master/property_feature_distribution.PNG "Number of properties with features")
![alt text](https://github.com/TKEnganeer/ds_zoop_proj/blob/master/property_location_distribution.PNG "Number of properties by location")
![alt text](https://github.com/TKEnganeer/ds_zoop_proj/blob/master/property_type_distribution.PNG "Number of properties types")


## Model Building 

I started by transforming the categorical variables into dummy variables. The data was split into train and test sets at a ratio at 80:20 respectively.   

I used three different models and evaluated them using Mean Absolute Error (MAE). Using MAE allowed me to interpret the results with relative ease as they are known to work well for these types of models.   

I tried the following three models:
*	**Multiple Linear Regression** – The baseline model
*	**Lasso Regression** – As the data is sparse and has many categorical variables,  a normalized regression like lasso might be effective.
*	**Random Forest** – Like lasso regression, with the sparsity associated with the data, I it has been shown that this a good model. 

## Model performance
The Random Forest model was only slightly better than Lasso other when it came to the test and validation sets. My Linear regression error was way to high compared to the other models which leads me to belive that there is either an error in my code or the data used to calculate the model.
*	**Random Forest** : MAE = -19.52
*	**Multi-Linear Regression**: MAE = -186336976912.14767
*	**Lasso Regression**: MAE = -19.55

## Productionization 
In this section, I built a flask API endpoint, hosted on a local webserver by folling the steps in the Flask Productionization tutorial referenced above. The API endpoint takes in a request with a list of values from the house criteria and returns the estimated price. 

