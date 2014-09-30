#Sean Nicholls
#30/09/14
#SAC EX3

day=int(input("Please enter the day in number format e.g '14' : "))
month=int(input("Please enter the month in number format e.g 'july = 7' : "))
year=int(input("Please enter the year in 2 digit format e.g '05' :"))

if month == 1:
    month1= ("January")
elif month ==2:
    month1= ("Febuary")
elif month ==3:
    month1 = ("March")
elif month ==4:
    month1 = ("April")
elif month ==5:
    month1 = ("May")
elif month ==6:
    month1 = ("June")
elif month ==7:
    month1 = ("July")
elif month ==8:
    month1 = ("August")
elif month ==9:
    month1 = ("September")
elif month ==10:
    month1 = ("October")
elif month ==11:
    month1 = ("November")
elif month ==12:
    month1 = ("December")

if year >=31 and year <=99:
    year1= ("19{0}".format(year))
elif year >=0 and year <=30:
    year1= ("20{0}".format(year))
else:
    year1 = ("Year is not in range")
    
print (" The date is the {0}th of {1} {2}".format(day, month1, year1))
