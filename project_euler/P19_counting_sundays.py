# I've decided to solve problem 19 using only the information given and not resorting to python's date and time functions
# The strategy is to generate all the dates and then count the number of Sundays on the first of the month in the desired period (20th century - 1901-200).


#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
def is_leap(year):
  if year % 100 == 0:
    return year % 400 == 0
  else:
    return year % 4 == 0

months = [
 ["Jan", 31],
 ["Feb", 28],
 ["Mar", 31],
 ["Apr", 30],
 ["May", 31],
 ["Jun", 30],
 ["Jul", 31],
 ["Aug", 31],
 ["Sep", 30],
 ["Oct", 31],
 ["Nov", 30],
 ["Dec", 31]
]

days_of_week = {
 0: "Sunday",
 1: "Monday",
 2: "Tuesday",
 3: "Wednesday",
 4: "Thursday",
 5: "Friday",
 6: "Saturday"
}

sundays_count = 0

day_of_week_idx = 1 # 1 Jan 1900 was a Monday.

for year in range(1900, 2001):
  if is_leap(year):
    months[1][1] = 29
  else:
    months[1][1] = 28

  for month in months:
    for day in range(1, month[1] + 1):
      # even though I'm generating dates from 01-01-1900 I'm just counting from 01-01-1901
      if year >= 1901 and days_of_week[day_of_week_idx] == 'Sunday' and day == 1:
        sundays_count += 1
      day_of_week_idx = (day_of_week_idx + 1) % 7


print('There were ' + str(sundays_count) + ' Sundays on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000).')
