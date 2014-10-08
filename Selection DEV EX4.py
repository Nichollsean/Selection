#Sean Nicholls
#8/10/14
#Selection DEV EX4

grade = int(input("How many marks did you get in the exam? "))

if grade >=0 and grade <=40:
    finalgrade = ("U")
elif grade >=41 and grade <=50:
    finalgrade = ("E")
elif grade >=51 and grade <=60:
    finalgrade = ("D")
elif grade>=61 and grade <=70:
    finalgrade = ("C")
elif grade>=71 and grade <=80:
    finalgrade = ("B")
elif grade>=81 and grade <=100:
    finalgrade = ("A")

print("You test score as a grade is a {0} grade".format(finalgrade))

