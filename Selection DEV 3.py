#Sean Nicholls
#7/10/14
#Development EX3

hoursworked=int(input("How many hours have you worked this week "))
hourlypay=float(input("How much do you get paid per hour normally "))

if hoursworked <=40:
    finalpay=(hoursworked*hourlypay)
elif hoursworked >=40:
    finalpay=(hoursworked*(1.5*hourlypay))

print("You have earned {0} this week".format(finalpay))


