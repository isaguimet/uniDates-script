import datetime
from datetime import timedelta 

# Using this as help: https://www.w3schools.com/python/python_datetime.asp
# http://www.pressthered.com/adding_dates_and_times_in_python/

x = datetime.datetime(2020, 9, 4)

# 1st day of university - Sept 8th. However, Sept 7th is a Monday
# Note: days=3 b/c this script was created on Sept. 4th
date = x + timedelta(days=3)

# Month name - Short version: ex: Sep
abbrevMonth = date.strftime("%b")

# Day of month 01-31
abbrevDay = date.strftime("%d")

i = 1

while (i < 15):
    if (abbrevDay == "01" or abbrevDay == "21" or abbrevDay == "31"):
        prefix = "st"
    elif (abbrevDay == "02" or abbrevDay == "22"):
        prefix = "nd"
    elif (abbrevDay == "03" or abbrevDay == "23"):
        prefix = "rd"
    else:
        prefix = "th"

    print("Week " + str(i) + ": " + abbrevMonth + ". " + abbrevDay + prefix)
    date = date + timedelta(days=7)
    abbrevMonth = date.strftime("%b")
    abbrevDay = date.strftime("%d")
    i = i + 1
