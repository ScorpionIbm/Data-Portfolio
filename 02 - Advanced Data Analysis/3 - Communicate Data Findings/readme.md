# (Prosper Loan data exploration)
## by (Islam Bakry Mohyee)


## Dataset

- This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others.

## Summary of Findings

- The main feature of interest in a loan dataset is the loan status that represents the current state of the loan whether it is in default ['Chargedoff', 'Defaulted', 'Past Due','Past Due (91-120 days)', 'Past Due (>120 days)'] or performing.
- As a risk analyst, I am interested in factors that can help predict the default status of loans:  
These factors are mainly: Score/Rating given by prosper (represented by multiple columns), income(stated income and income range), residential status, employment (status and duration), borrower rate.


- We then go on to inspect the distribution of all our variables.  
- Then we check the relation between all of our variables and the main variable of interest:  
    - The relation between the NPL variable and the credit rating variables (CreditScoreRange, ProsperRating, CreditGrade) is one of the strongest relations in the dataset which is obvious because is is one of the main aspects of the credit process.  
    - The annual rate is higher for customers in the NPL group due to them being rated in higher risk which entails higher rates  
    - The distribution of income (after a log transformation) is mostly the same across both categories but there's a slight upward shift of income in the PL category which indicates the weak relation that customers with higher income perform better on repayment.  


- **While checking for interesting correlation between other factors within the dataset:**  
    - We noticed a relation between Prosper score and Borrower APR, this shows that customers who get higher scores are generally charged a lower rate.  
    - By checking the chart it obviously shows the strong negative relation between the borrower rate and the scores assigned by prosper, where a customer with higher score is charged a lower rate.


- Then we go on to check for the relation between three variables together.

    - **The weak relation between <u>Score ranges</u> and <u>annual income</u> across the categories of <u>PL and NPL</u> (our variable of interest).**  
        - It shows how customers with higher income take higher scores.  
        - Within each score range, the ones who are performing (PL) generally have more income than those who are NPL (as shown by the median of each box)
    - **The relation between <u>Score ranges</u> and the <u>charged annual rate</u> across the categories of <u>PL and NPL</u> (our variable of interest).**  
        - It shows how customers with higher scores are generally charged lower annual rates.  
        - Within each score range, the ones who are performing (PL) are charged rates lower than those who are NPL (as shown by the median of each box) especially in the higher score categories  

- **One surprising interaction between features that we noticed**

    - **The relation between <u>Prosper scores</u> and the <u>charged annual rate</u> across the categories of <u>PL and NPL</u> (our variable of interest).**  
        - It shows how customers with higher scores are generally charged lower annual rates.  
        - A much higher distinction between the PL and NPL than the one with score range.  
        - The higher distinction between PL and NPL within the Scores is due to the interaction between the three variables as the Prosper score has higher correlation with the charged annual rates than the Score ranges although the Score ranges have better correlation with NPL than the Prosper score.

## Key Insights for Presentation

For the presentation, I just focus on the variable of interest (NPL) and two other factors: the credit score range and Borrower APR. 
I start by inspecting the distribution of all three vraiables.

Then using a barchart I check the relation between the APR and the NPL status 
and use facetted countplots to check the difference in distribution of Credit Scores across both groups of NPL status 

Then I go on to inspect the relation between the three variables together and show that:
- Customers with higher scores are generally charged lower annual rates.  
- Within each score range, the ones who are performing (PL) are charged rates lower than those who are NPL (as shown by the median of each box) especially in the higher score categories  


## Sources

### I modified the codes for some plots in the explanatory slides but they give the same output plots

### I used the following command to export to slidedeck 

> jupyter nbconvert exploration_template.ipynb --to slides --no-input

It clears input from the slides

### I used a code snippet from here to center output in the notebook but it didn't work with the slides

> https://stackoverflow.com/questions/18380168/center-output-plots-in-the-notebook

### I used the following stack posts as guides with the documentation to plot subplots and modify the spacing

https://stackoverflow.com/questions/10388462/matplotlib-different-size-subplots
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots-in-matplotlib
https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html

### Modifying properties of subplots with axis properties
https://matplotlib.org/stable/api/axes_api.html#axis-labels-title-and-legend

