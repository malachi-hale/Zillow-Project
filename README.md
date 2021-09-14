# Regression Project
## Predicting the value of Southern California single-unit properties 

## Objectives 
### Project Goals 
 - To document **code**, **process**, **findings, and **key takeaways** in a Jupyter Notebook report. 
 
 - To create modules such as `acquire.py` and `prep.py` which contain functions that make our process repeatable.
 
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
 
 - **Conclusion:** We rejected the null hypothesis and concluded that there is a correlation between square feet and tax value of a property. 
 
### Hypothesis 2 
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant correlation between bedroom count and tax value. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant correlation between bedroom count and tax value. 
 
 - **Conclusion:** We rejected the null hypothesis and concluded that there is a correlation between bedroom count and tax value.
 
### Hypothesis 3
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant correlation between bathroom count and tax value. 
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant correlation between bathroom count and tax value. 
 
 - **Conclusion:** We rejected the null hypothesis and concluded that there is a correlation between bathroom count and tax value. 
 
### Hypothesis 4 
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant difference in `taxvaluedollarcnt` for homes in Los Angeles County (FIPS code 6037) and homes Orange County (FIPS code 6111).  
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant difference in `taxvaluedollarcnt` for homes in Los Angeles County (FIPS code 6037) and homes in either Orange County (FIPS code 6111).
 
 - **Conclusion:** We rejected the null hypothesis and concluded that there is a significant difference in `taxvaluedollarcnt` for homes in Los Angeles County and Orange County. 
 
### Hypothesis 5 
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant difference in `taxvaluedollarcnt` for homes in Los Angeles County (FIPS code 6037) and homes Ventura County (FIPS code 6111).  
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant difference in `taxvaluedollarcnt` for homes in Los Angeles County (FIPS code 6037) and homes in either Ventura County (FIPS code 6111).
 
 - **Conclusion:** We rejected the null hypothesis and concluded that there is a significant difference in `taxvaluedollarcnt` for homes in Los Angeles County and Ventura County. 
 
### Hypothesis 6
 - **alpha** = 0.05
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no significant difference in `taxvaluedollarcnt` for homes in Orange County (FIPS code 6037) and homes Ventura County (FIPS code 6111).  
 
 - ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a significant difference in `taxvaluedollarcnt` for homes in Orange County (FIPS code 6037) and homes in either Ventura County (FIPS code 6111).
 
 - **Conclusion:** We rejected the null hypothesis and concluded that there is a significant difference in `taxvaluedollarcnt` for homes in Orange County and Ventura County. 
 
## Executive Summary - Conclusions and Next Steps 
 - With the goal of determining the features most predictive of `taxvaluedollarcnt`. Using the methods Select K Best and Recursive Feature Elimination. Both of these methods indicated that the top three features most predictive of `taxvaluedollarcnt` were `calculatedfinishedsquarefeet`, `bedroomcnt`, and `bathroomcnt`.
 
 - I used the features `calculatedfinishedsquarefeet`, `bedroomcnt`, and `bathroomcnt` to predict `taxvaluedollarcnt` utilizing the following models: 
      - Linear Regression, 
      - LassoLars, and
      - TweedieRegressor. 
 
 - Based on the RMSE for the TweedieRegressor model, I used this model to predict `taxvaluedollarcnt` for our `test` dataset. 
 
## Pipleline Stages Breakdown 

### Project planning 
 - Create a `READ.md` file with an outline of a plan for the project. 
 - Brainstorm ideas and form hypothesis related to how variables relate or impact each other. 
 
### Data Acquisition
**In the `acquire.py` file**
 - Create an `acquire.py` file that is reproducible for gathering data from a database using SQL and reading this data into a pandas DataFrame. 

 - In the `acquire.py` we will have functions to impute null values and to remove outliers from the dataset. 

**In the Notebook**
 - Utilize the `acquire.py` file to obtain a pandas DataFrame that contains the relevant data. 
 
 - Complete initial data summarization (`info()`, `describe()`).
 
 - Plot distributions of individual variables. 
 
### Data Preparation
**In the `prep.py` module**
 - split data into `train`, `validate`, `test` datasets. 
 
 - use the min max scaler to scale the `calculatedfinishedsquarefeet`, `bedroomcnt`, and `bathroomcnt` columns. 
 
**In the Notebook**
 - Import the `prep.py` file and use the functions to prepare the data for the notebook. 
 
 - Take a sample of the the newly cleaned data. 
 
### Data Exploration and Analysis
**In the Notebook**
 - Answer the key questions posed by hypotheses. 
 
 - Run correlation tests and t-tests on the data. 
 
 - Visualize all combinations of variables in some way. 
 
 - Determine what independent variables are correlated with other independent variables?
 
 - Summarize key takeaways and conclusions. 

### Feature engineering
**In the Notebook**
 - Utilize Select K Best and Recursive Feature Elimination to determine which features are most predictive of `taxvaluedollarcnt`.

### Modeling 
**In the Notebook**
 - Establish a baseline model. Show how the model I end up with performs better. 
 
 - Documenting the various algorithms and hyperparameters used along with evaluation codes and results. 
 
 - Evaluate the model using standard techniques. Compute the evaluation metrics, compare models to baseline, etcetera. 
 
## Reproduce my project 
To reproduct my project, you will need your own `env.py` file with database credentials, in addition to the files listed below: 
 - Read this `READ.md` file.
 - Download the `acquire.py`, `prep.py` and `Final_Project.ipynb` files. 
 - Add your own `env.py` file to your directory. You will need to access the SQL database to access the Zillow data.
 - Run the `Final_Project.ipynb` notebook. 
