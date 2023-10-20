#1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements

# To get year from the user
year=int(input("Enter a year : "))

#For direct declaration of value 
'''year=2015'''

# century year divided by 400 is leap year
if (year%400==0 and year%100==0):
    print("{0} is a leap year".format(year))

# if it is not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year%4==0 and year%100!=0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 and 4,year is not leap year
else:
    print("{0} is not a leap year".format(year))
