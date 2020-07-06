#Right Traingle Solver App

#importing Library
from math import sqrt

#Welcome msg
print("Welcome to the Right Traingle Solver App")

#Gathering Information
First_len = float(input("\nWhat is the First Length of the Traingle: "))
Second_len = float(input("What is the Second Length of the Traingle: "))

#formula calculation
hypotenuse = sqrt(pow(First_len, 2)+pow(Second_len, 2))
Area = 0.5*First_len*Second_len

#Round off upto 3 Decimal
hypotenuse = round(hypotemuse, 3)
Area = round(Area, 3)

#Displaying Results
print("\nFor a Triangle with length of "+str(First_len)+" and "+str(Second_len)+ " the Hypotenuse is " + str(hypotenuse)+ " . ")
print("For a Triangle with length of "+str(First_len)+" and "+str(Second_len)+ " the Area is " + str(Area)+ " . ")
