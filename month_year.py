#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 11th, 2022
# This program asks the user to enter a number for a month and year. 
# It then tell you what month
# the number corresponds to and how many days are in that month.


def main():
    # get month and year from the user
    user_month = input("Enter a month (i.e 1 represents January): ")
    user_year = input("Enter a year: ")
    print("")

    try:
        # Changing string into integer
        user_month_as_int = int(user_month)
        user_year_as_int = int(user_year)
        
        # set a range
        if user_year_as_int < 1:
            print("Please enter a positive number.")
        elif user_month_as_int > 12:
            print("Please enter a number that represents a month")
        else:

            # check to see if what user_month enters corresponds to a month
            if user_month_as_int == 1:
                print("January {} has 31 days". format(user_year))
            elif user_month_as_int == 2:
                print("February {} has 30 days". format(user_year))
    
            elif user_month_as_int == 3:
                print("March {} has 28 days". format(user_year))
    
            elif user_month_as_int == 4:
                print("April {} has 30 days". format(user_year))
    
            elif user_month_as_int == 5:
                print("May {} has 31 days". format(user_year))
    
            elif user_month_as_int == 6:
                print("June {} has 30 days". format(user_year))
    
            elif user_month_as_int == 7:
                print("July {} has 31 days". format(user_year))
    
            elif user_month_as_int == 8:
                print("August {} has 31 days". format(user_year))
    
            elif user_month_as_int == 9:
                print("September {} has 30 days". format(user_year))
    
            elif user_month_as_int == 10:
                print("October {} has 31 days". format(user_year))
    
            elif user_month_as_int == 11:
                print("November {} has 30 days". format(user_year))
    
            elif user_month_as_int == 12:
                print("December {} has 31 days". format(user_year))
    
            else:
                print("Please enter a valid month.")

    except Exception:
        print("{} is not a month or year.". format(user_year))


if __name__ == "__main__":
    main()
