#Sean Nicholls
#7/10/14
#Selecion DEV EX2


temp=float(input("What is the temperature of your water: "))

if temp <=0:
    result=("Frozen")
elif temp >=1 and temp <=99:
    result= ("Neither")
elif temp >=100:
    result=("Boiling")


print("Your water is {0} ".format(result))

