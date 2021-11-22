#/usr/bin/python

import json
import yaml

#from datetime import date
#from datetime import datetime
#from datetime import timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *


with open('budget.yaml') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)

full_budget = {}
x_list = []
y_list = []
today = date.today()
day_of_year = datetime.now().timetuple().tm_yday
day_of_month = datetime.now().timetuple().tm_mday
day_of_week = datetime.now().timetuple().tm_wday
start_date = today.strftime("%Y-%m-%d")
enddate = today + relativedelta(years=1)
print(today)
print(day_of_year)
print(day_of_month)
print(day_of_week)
print(enddate)
print(type(enddate))

print(data)

for transaction in data["transactions"]:
  if len(transaction) != 6:
    exit("Not enough entries in transaction")
  transaction_type = transaction[0]
  name = transaction[1]
  unit = transaction[2]
  interval = transaction[3]
  day = transaction[4]
  amount = transaction[5]
  if unit == "month" and ( day > 28 or day < 1 ):
    exit("Can't repeat every " + str(day) + " of the month")
  if unit == "week" and ( day > 7 or day < 1):
    exit("Can't repeat every " + str(day) + " of the week")
  if unit == "year" and ( day > 365 or day < 1):
    exit("Can't repeat every " + str(day) + " of the year")
  if unit not in ["week", "month", "year", "day"]:
    exit("Can only use week, month, or year for unit")
  if unit == "month":
    unit = "MONTHLY"
    count = int(24 / interval)
    datelist = list(rrule(MONTHLY, interval=interval, count=count, dtstart=parse(start_date)))
  if unit == "week":
    unit = "WEEKLY"
    count = int(104 / interval)
    datelist = list(rrule(WEEKLY, interval=interval, count=count, dtstart=parse(start_date)))
  if unit == "day":
    unit = "DAILY"
    count = int(730 / interval)
    datelist = list(rrule(DAILY, interval=interval, count=count, dtstart=parse(start_date)))
  if transaction_type == "expense":
    multiplier = -1
  else:
    multiplier = 1
  print("You spend " + str(amount) + " dollars every " + str(interval) + " " + unit + "s? That's a lot!")
  for transaction_d in datelist:
    transaction_date = transaction_d.strftime("%Y-%m-%d")
    print(name + " " + transaction_date + " " + str(amount * multiplier))
    if transaction_date not in full_budget:
      full_budget[transaction_date] = {}
    full_budget[transaction_date][name] = amount * multiplier
    

for transaction_date in sorted(full_budget):
  #print(transaction_date)
  sum = 0
  for k, v in full_budget[transaction_date].items():
    sum += v
  full_budget[transaction_date]["sum"] = sum
  print(transaction_date + " " + str(sum))
  x_list.append(transaction_date)
  y_list.append(sum)

endlist = [
  {
    "x": x_list,
    "y": y_list,
    "type": "scatter"
  }
]

with open('./mydata.json', 'w') as f:
  json.dump(endlist, f)

#print(full_budget)

#[
#  {
#    x: ['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],
#    y: [1, 3, 6],
#    type: 'scatter'
#  }
#];
