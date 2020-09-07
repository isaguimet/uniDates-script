import datetime
from datetime import timedelta 

# To create a list of all the weeks and dates of a particular semester, 
# simply put the dates (line 11) of the first Monday of the first week of the semester

# Used these links for resources: https://www.w3schools.com/python/python_datetime.asp
# http://www.pressthered.com/adding_dates_and_times_in_python/

# Date of first Monday of the first week of the semester. For Fall 2020: Sept 7th
date = datetime.datetime(2020, 9, 7)

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

    # adds 7 days (1 week) to the current date
    date = date + timedelta(days=7)

    abbrevMonth = date.strftime("%b")
    abbrevDay = date.strftime("%d")
    i = i + 1
