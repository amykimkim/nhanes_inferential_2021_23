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
- To investigate how age and marital status affect systolic blood pressure, I first loaded and merge the relevant datasets (blood pressure, age, and marital status). 
- Then, I cleaned the marital status column as before. 
- I used a multiple linear regression model to quantify the individual and combined effects of age and marital status on systolic blood pressure.
- Average difference in systolic blood pressure between individuals who are 'not married' compared to the 'married' group is 1.342 
- systolic blood pressure is expected to change for every one-year increase in age by 0.3952
- R squared value of 0.134 indicates that approximately 13.4% of the variation in the dependent variable can be explained by the independent variable
- Both P-values for marital status and age was less than 0.05, suggesting that the predictor has a statistically significant effect on systolic blood pressure.

## Question 4 PYTHON:
- To investigate if weight and minutes of sedentary behavior has a correlation, I first loaded and merged the relevant datasets
- A Pearson correlation coefficient was used for the two continuous variables (self-reported weight and minutes of sedentary behavior) to measure the strength and direction of a linear relationship between them
- Pearson correlation between self-reported weight and sedentary behavior: 0.1560. Suggests that there is no linear relationship between self-reported weight and sedentary behavior. But correlation does not imply causation

## Question 5 PYTHON (creative analysis): Is there a correlation between hepatitis B lab Antibodies (LBXHBS) and minutes of sedentary behavior (PAD680)?
- Cleaned the LBXHBS column by converting positive (1.0) to 1 and negative (2.0) to 0, and ensure both columns are free of missing values