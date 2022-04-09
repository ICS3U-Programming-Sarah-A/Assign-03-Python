#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 5th, 2022
# This program asks the user to  guess a number. It then generates a
# random number. It also checks to see if user guess is a valid number entered 
# to determine if user guess is == rand num. 


def main():
    # get number guessed from user
    user_month = input("Enter a month (i.e 1 represents January): ")
    user_year = input("Enter a year: ")
    print("")

    try:
        # Changing string into integer
        user_month_as_int = int(user_month)
        user_year_as_int = int(user_year)
        # check to see if user guess == random number
        if user_month_as_int == 1:
          print("January {}". format(user_year), "has 31 days")
        elif user_month_as_int == 2:
            print("Febuary {}". format(user_year), "has 30 days")
       
        elif user_month_as_int == 3:
            print("March {}". format(user_year), "has 31 days")
       
        elif user_month_as_int == 4:
            print("April {}". format(user_year, "has 30 days")
            
        elif user_month_as_int == 5:
            print("May {}". format(user_year), "has 31 days")
       
        elif user_month_as_int == 6:
            print("June {}". format(user_year), "has 30 days")
       
        elif user_month_as_int == 7:
            print("July {}". format(user_year), "has 31 days")
       
        elif user_month_as_int == 8:
            print("August {}". format(user_year), "has 31 days")
        
        elif user_month_as_int == 9:
            print("September {}". format(user_year), "has 30 days")
        
        elif user_month_as_int == 10:
            print("October {}". format(user_year), "has 31 days")
       
        elif user_month_as_int == 11:
            print("November {}". format(user_year), "has 30 days")
       
        elif user_month_as_int == 12:
            print("December has 31 days")
        
        else: 
          print("Please enter a valid number")
          
    except Exception:
        print("{} is not a number.". format(user_month))


if __name__ == "__main__":
    main()