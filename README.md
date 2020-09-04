# Data Science Outer London House Price Estimator: Project Overview
* Created a tool to estimate the house prices for propeties < 40 miles from central London less than £325k (MAE ~ £19K) to help people when looking for homes at commutable distance. 
* Scraped over 900 property descriptions from zoopla.co.uk using python and beautifulsoups.
* Engineered features from the text of each decsription to quantify the value house prices have on garden, largeness, spaciousness and whether or notthe propety has been extended.
* Optimised Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

## Code and Resources Used
**Python Version:** 3.8

**Packages:** pandas, numpy, sklearn, maatplotlib, seasborn, beautifulsoups, flask, json, pickle.

**For Web Framework Requirements:** pip install -r requirements.txt

**Data Science Project Tutorial Series:** https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

**Scraper Tutorial:** https://www.youtube.com/watch?v=Itqfkgw508U

**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping
I adapated the web scraper from the youtube video (above) to suit my a search creteria - A 3 bedroom house with a maximum 40miles from central London under £325k. I used this information to scrape about 900 property information postings on zoopla.co.uk. I got the following information from each property:
* title 
* address 
* description 
* price 
* estate agent phone number
* closest_station (to property)
* listed_on (date listed) 
* image (of property)
* closest_st_miles (distance to closest train station)
* prop_pc (postcode) 

## Data Cleaning

After scraping the data, I cleaned so it could be more usable in my model. I made the following changes and created the following variables: 
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

![alt text]

## Model Building

## Model Performance

## Productionization

