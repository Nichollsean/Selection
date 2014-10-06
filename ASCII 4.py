#Sean Nicholls
#6/10/14
#ASCII Exercise 4

asking=print("Please enter an 7 bit binary string below")
string=(input(""))
yesparity=1
noparity=0

part1=string[0:1]
part2=string[1:2]
part3=string[2:3]
part4=string[3:4]
part5=string[4:5]
part6=string[5:6]
part7=string[6:7]

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

total= finalans1+finalans2+finalans3+finalans4+finalans5+finalans6+finalans7

if total==0:
    print("{0}{1}{2}{3}{4}{5}{6}{7} is your answer using the odd parity".format(yesparity, part1, part2, part3, part4, part5, part6, part7))
elif total==2:
          print("{0}{1}{2}{3}{4}{5}{6}{7} is your answer using the odd parity".format(yesparity, part1, part2, part3, part4, part5, part6, part7))
elif total==4:
    print("{0}{1}{2}{3}{4}{5}{6}{7} is your answer using the odd parity".format(yesparity, part1, part2, part3, part4, part5, part6, part7))
elif total==6:
    print("{0}{1}{2}{3}{4}{5}{6}{7} is your answer using the odd parity".format(yesparity, part1, part2, part3, part4, part5, part6, part7))

if total==1:
    print("{0}{1}{2}{3}{4}{5}{6}{7} is your answer using the odd parity".format(noparity, part1, part2, part3, part4, part5, part6, part7))
elif total==3:
    print("{0}{1}{2}{3}{4}{5}{6}{7} is your answer using the odd parity".format(noparity, part1, part2, part3, part4, part5, part6, part7))
elif total==5:
    print("{0}{1}{2}{3}{4}{5}{6}{7} is your answer using the odd parity".format(noparity, part1, part2, part3, part4, part5, part6, part7))
elif total==7:
    print("{0}{1}{2}{3}{4}{5}{6}{7} is your answer using the odd parity".format(noparity, part1, part2, part3, part4, part5, part6, part7))
