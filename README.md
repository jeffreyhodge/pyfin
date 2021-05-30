# pyfin
Running expense tracker

## Plan

Show how much money you should have at any given point in time based on income and expenses

### functionality
* import list of expenses from yaml file, excel file, and UI
* allow for hypotheticals/what ifs
* allow for editing
* get a starting value
* add income and subtract expenses in order and display current balance as metric on time series graph

### format of budget
expense name, category name, schedule, amount (maybe allow to be percentage of another expense or income)

### schedule needs to handle
* n times per month/year
* each month on 10 (must be 1-28) or negative to do days counting backwards from end of month
* each year on 06-04
* every n weeks/months/years
* every 2 weeks starting on 2021-06-04

### display
* pie chart of expenses
* graph of cash flow
