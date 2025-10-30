# nhanes_inferential_2021_23

## Question 1 PYTHON:
- I loaded in the xpt file 
- I cleaned the data for 'DMDMARTZ' so that there are two categories: married and unmarried. Left out the nulls
- Did the same thing for education level 'DMDEDUC2' so that it is categorized into either less than bachelor's or bachelor's degree and/or greater
- After data cleaning, since it is for two categorical values, I decided to perform a chi-square test to see if there's a relationship between married status and education level
- Result: Chi-square statistic: 129.1738, P-value: 0.0000 --> would indicate a significant association between marital status and education level since it is less than 0.05

## Question 2 PYTHON:
- I loaded in the xpt file 
- I cleaned the data for 'PAD680' to remove values 7777, 9999, and null
- T-test to compare the means of two independent groups
T-statistic: nan
P-value: nan
There is no statistically significant difference in the mean sedentary behavior time between married and not married individuals.

## Question 3 PYTHON:
To investigate how age and marital status affect systolic blood pressure, I will first load and merge the relevant datasets (blood pressure, age, and marital status). Then, I will clean the marital status column as before. Finally, I will use a multiple linear regression model to quantify the individual and combined effects of age and marital status on systolic blood pressure.