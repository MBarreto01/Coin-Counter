 #------------------------------------------------------ 
 # Programmer: Michael Barreto
 # Course:     COSC 1315 Section 010           
 #------------------------------------------------------

 # Declare 'constants' to be used in the program
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

 # Prompt the user for the number of pennies, nickels,
 # dimes, and quarters
numPennies = int(input("Enter the number of pennies: "))
numNickels = int(input("Enter the number of nickels: "))
numDimes = int(input("Enter the number of dimes: "))
numQuarters = int(input("Enter the number of quarters: "))

# Sum up the total value in cents for the entered
# pennies, nickels, dimes, and quarters

totalCentValue = (numPennies * PENNY_VALUE) + \
                 (numNickels * NICKEL_VALUE) + \
                 (numDimes * DIME_VALUE) + \
                 (numQuarters * QUARTER_VALUE)

# Calculate the total value in dollars
totalDollars = totalCentValue / PENNIES_IN_DOLLAR

# Determine whether the user has 'won' the game

# The amount was more than one dollar. Print out a message
# indicating the amount that the user entered,
# and then amount that was over a dollar. Format the numbers

if totalDollars > 1.0:
    print("\nSorry, the amount you entered was more than one dollar.")
    print("Your amount was $", format(totalDollars, '.2f'))
    print("In fact, it was $", format(totalDollars - 1.0, '.2f'), \
                                      "over a dollar")
    
# The amount was less than one dollar. Print out a message
# indicating this, the amount that the user entered, and the
# amount that was under a dollar. Format the numbers

elif totalDollars < 1.0:
    print("\nSorry, the amount you entered was less than one dollar.")
    print("Your amount was $", format(totalDollars, '.2f'))
    print("In fact, it was $", format(1.0 - totalDollars, '.2f'), \
          "under a dollar.")

# The amount was exactly one dollar. Print out a message
# indicating this

else:
    print("\nCONGRATULATIONS!!!")
    print("The amount you entered was exactly one dollar!")
    print("You win the game!")

print("\nThis program was written by Michael Barreto.")
print("End of program.")
          
