import datetime
from datetime import timedelta 

# To create a list of all the weeks and dates of a particular semester, 
# simply put the dates (line 11) of the first Monday of the first week of the semester

# Used these links for resources: https://www.w3schools.com/python/python_datetime.asp
# http://www.pressthered.com/adding_dates_and_times_in_python/

# Date of first Monday of the first week of the semester. For Winter 2021: January 11th
date = datetime.datetime(2021, 1, 11)

# Month name - Short version: ex: Sep
abbrevMonth = date.strftime("%b")

# Day of month 01-31
abbrevDay = date.strftime("%d")

i = 1

# Open file to store dates in, "w" stands for overwrite
datesStoredFile = open("unidatesText.txt", "w")

datesStoredFile.write("Here are the dates for the Winter 2021 Semester! \n\n")

while (i < 15):
    if (abbrevDay == "01" or abbrevDay == "21" or abbrevDay == "31"):
        prefix = "st"
    elif (abbrevDay == "02" or abbrevDay == "22"):
        prefix = "nd"
    elif (abbrevDay == "03" or abbrevDay == "23"):
        prefix = "rd"
    else:
        prefix = "th"

    # Writes all the dates for all the weeks in the semester to a .txt file
    datesStoredFile.write("Week " + str(i) + ": " + abbrevMonth + ". " + abbrevDay + prefix + "\n")

    # Write all the dates for all the weeks in the semester to the command line interface
    print("Week " + str(i) + ": " + abbrevMonth + ". " + abbrevDay + prefix)

    # adds 7 days (1 week) to the current date
    date = date + timedelta(days=7)

    abbrevMonth = date.strftime("%b")
    abbrevDay = date.strftime("%d")
    i = i + 1

# closes the unused file
datesStoredFile.close()
