from decimal import Decimal

MaxPointsPossible = 57

name = "Rastin"

score = 39

percentage = (score / MaxPointsPossible)*100

if percentage<=100 and percentage>=90:
    grade = "A"
elif percentage<90 and percentage>=80: 
    grade = "B"
elif percentage<80 and percentage>=70: 
    grade = "C"
elif percentage<70 and percentage>=60: 
    grade = "D"
elif percentage<60 and percentage>=50:
    grade = "E"
elif percentage<0:
    grade = "ERROR"
else:
    grade = "F"
    
# First we take a float and convert it to a decimal
decimalPercentage = Decimal(percentage)

# Then we round it to 2 places
roundedPercentage = round(decimalPercentage,2)

print("{} got a percentage of {} and a grade of {}".format(name, roundedPercentage, grade))
