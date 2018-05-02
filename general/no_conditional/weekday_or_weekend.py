# from: https://medium.com/@samerbuna/coding-tip-try-to-code-without-if-statements-d06799eed231
#
# Solve the problem without using if-statements (or ternary operators, or switch statements).
#
# Challenge #2: The weekendOrWeekday function
# Write a function that takes a date object argument (like new Date()) and returns the string “weekend” or “weekday”.



import datetime

week_days = {
0: 'weekday',
1: 'weekday',
2: 'weekday',
3: 'weekday',
4: 'weekday',
5: 'weekend',
6: 'weekend',
}

def weekday_or_weekend(d):
    print week_days[d.weekday()]

weekday_or_weekend(datetime.datetime.now())
