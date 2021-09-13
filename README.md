# Regression Project
## Predicting the value of Southern California single-unit properties 

## Objectives 
### Project Goals 
 - To document **code**, **process**, **findings, and **key takeaways** in a Jupyter Notebook report. 
 
 - To create modules such as `acquire.py` and `prepare.py` which contain functions that make our process repeatable.
 
 - To construct a model that predicts the tax value of a property using regression techniques. 
 
 - To deliver a five-minute presentation of a high-level walkthrough of a Jupyter Notebook. 
 
### Business Goals 
  - To predict the tax value of single unit properties with a transaction date in May-August 2017 in Los Angeles, Orange, and Ventura County. 
  
  - To calculate the tax rates for each county the properties are located in. 

### Audience 
 - The Zillow data science team. 
  
## Data Dictionary 

| Feature                             | Dataype   | Definition                                                     |
|:------------------------------------|:----------|:---------------------------------------------------------------|
| bedroomcnt                          | float64   | Total number of bedrooms in the property                       |
| bathroomcnt                         | float64   | Total number of bathrooms in the property                      |
| calculatedfinishedsquarefeet        | float64   | Calculated square feet of the property                         |
| taxvaluedollarnct                   | float64   | Assessed dollar value of the property                          |
| yearbuilt                           | float64   | Year the property was originally built                         |
| taxamount                           | float64   | Total amount of properties taxes per year in dollars           |
| fips                                | float64   | FIPS code, indicating the county the property is located in    |
| calculatedfinishedsquarefeet_scaled | float64   | Square feet, scaled so that all values are between 0 and 1     |
| bedroomcnt_scaled                   | float64   | Bedroom count, scaled so that all values are between 0 and 1   |
| bathroomcnt_scaled                  | float64   | Bathroom count, scaled so that all values are betwween 0 and 1 |

## Initial Hypotheses

### Hypothesis 1 
 - **alpha** = 0.05
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant correlation between calculated finished square feet and tax value. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant correlation between calculated finished square feet and tax value. 
 
## Executive Summary - Conclusions and Next Steps 

