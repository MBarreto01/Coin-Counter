#------------------------------------------------------ 
# Programmer: Michael Barreto
# Course:     COSC 1315 Section 010
# Semester:   Spring 2022
# Assignment: 2b
# Due Date:   February 9th, 2022
#------------------------------------------------------

# Declare 'constants' to be used in program
SECONDS_DAY = 86400
SECONDS_HOUR = 3600
SECONDS_MINUTE = 60

# Initialize variables
hours = 0
days = 0
minutes = 0

# Prompt the user for the number of seconds
seconds = int(input("Enter the number of seconds : "))

# Calculate the number of days from these seconds
if seconds >= SECONDS_DAY:
    days = seconds // SECONDS_DAY
    daysRemainder = seconds % SECONDS_DAY

# Calculate the number of hours from these seconds
if seconds >= SECONDS_HOUR:
    hours = seconds // SECONDS_HOUR
    hoursRemainder = seconds % SECONDS_HOUR

# Calculate the number of minutes from these seconds
if seconds >= SECONDS_MINUTE:
    minutes = seconds // SECONDS_MINUTE
    minutesRemainder = seconds % SECONDS_MINUTE

# Print out the number of days, hours, minutes, and seconds
if minutes == 0:
    print("The number of seconds is less than one minute.")
    print("In fact, the number of seconds is:", seconds)

else:
    print(seconds, "seconds are equal to:")
    print(minutes, "full minute(s) and", minutesRemainder, "seconds.")
    
    if hours != 0:
        print(hours, "full hour(s) and", hoursRemainder, "seconds.")

    if days !=0 :
        print(days, "full day(s) and", daysRemainder, "seconds.")

print("/n This program was written by Michael Barreto.")
print("End of program.")
        
