## When will my savings generate enough interest to match my annual salary?
# There's a google sheet with the same calculation.
# https://docs.google.com/spreadsheets/d/1HMiiVHEw3gIoz6ref0NB4FjSQhMc4N93MfNQbcOYbCg/edit?usp=sharing


## All calculations are at yearly scale.

LAKH = 1 # regulate unit

INFLATION_RATE = 0.07 # 7%

INTEREST_RATE = 0.1 # 10%
EFFECTIVE_INTEREST_RATE = INTEREST_RATE - INFLATION_RATE

SALARY_GROWTH_RATE = 0.1 # 10%
EFFECTIVE_SALARY_GROWTH_RATE = SALARY_GROWTH_RATE - INFLATION_RATE

EARLY_YEARS = 5
EARLY_ANNUAL_SAVING_RATE = 0.2 # 20%
LATER_ANNUAL_SAVING_RATE = 0.7 # 70%

ANNUAL_SALARY = 10 * LAKH


def incomeGenerator(num_of_year):
  salary_values = [0]*num_of_year
  salary_values[0] = ANNUAL_SALARY
  for i in range(1, num_of_year):
    salary_values[i] = salary_values[i-1] * (1+EFFECTIVE_SALARY_GROWTH_RATE)
  return salary_values


def netWorthGenerator(num_of_year):
  salary_values = incomeGenerator(num_of_year)
  saving_values = [0] * (num_of_year + 1)
  amount_values = [0] * (num_of_year + 1)
  interest_values = [0] * (num_of_year + 1)
  for year in range(1, num_of_year+1):
    saving_rate = LATER_ANNUAL_SAVING_RATE
    if year < EARLY_YEARS:
      saving_rate = EARLY_ANNUAL_SAVING_RATE
    saving_values[year] = salary_values[year-1] * saving_rate
    interest_values[year] = amount_values[year-1]*(EFFECTIVE_INTEREST_RATE)
    amount_values[year] = interest_values[year] + amount_values[year-1] + saving_values[year-1]
    
    ## printing out
    saving_desp = "saving in Cr"
    if amount_values[year] < 100:
      saving_desp = "saving in Lk"
    print("year:", year, "salary:", salary_values[year-1], "interest:", interest_values[year], saving_desp, amount_values[year]/100 )

# This will print your salary, interest earned and total savings (net worth) with every year.
# Year in which your interest earned >= salary that's when you are free, i.e., you don't need
# to work for salary.
netWorthGenerator(70)


