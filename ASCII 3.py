#Sean Nicholls
#6/10/14
#ASCII 3

asking=print("Please enter an 8 bit binary string below")
string=(input(""))


part1=string[0:1]
part2=string[1:2]
part3=string[2:3]
part4=string[3:4]
part5=string[4:5]
part6=string[5:6]
part7=string[6:7]
part8=string[7:8]


if part1 == ("1"):
     finalans1=(1)
elif part1== ("0"):
     finalans1=(0)
if part2 == ("1"):
     finalans2=(1)
elif part2== ("0"):
     finalans2=(0)
if part3 == ("1"):
     finalans3=(1)
elif part3== ("0"):
     finalans3=(0)
if part4 == ("1"):
     finalans4=(1)
elif part4== ("0"):
     finalans4=(0)
if part5 == ("1"):
     finalans5=(1)
elif part5== ("0"):
     finalans5=(0)
if part6 == ("1"):
     finalans6=(1)
elif part6== ("0"):
     finalans6=(0)
if part7 == ("1"):
     finalans7=(1)
elif part7== ("0"):
     finalans7=(0)
if part8 == ("1"):
     finalans8=(1)
elif part8== ("0"):
     finalans8=(0)          


answertotal= finalans1+finalans2+finalans3+finalans4+finalans5+finalans6+finalans7+finalans8

if answertotal == 2:
     print("This code is valid")
elif answertotal == 4:
     print("This code is valid")
elif answertotal == 6:
     print("This code is valid")
elif answertotal == 8:
     print("This code is valid")

else:
     print("This code is not valid")


