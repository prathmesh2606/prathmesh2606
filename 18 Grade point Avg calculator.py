# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:55:08 2020

@author: Prathmesh
"""
# Welcome Message
print("================= Welcome to Average calculator App ===================")

name = input("Enter Your Name: ").title()
num = int(input("How Many Grades you like to enter? : "))
grades = []
for i in range(num):
    marks = float(input("Enter the Grades: "))
    grades.append(marks)

print("\nGrades Highest to Lowest")
grades.sort(reverse=True)
for grade in grades:
    print("\t",grade)
old_avg = round(sum(grades)/num,2)
print("\n",name,"'s Grade summary:")
print("\tTotal numbers of Grade:",num)
print("\tHighest Grade:",grades[0])
print("\tLowest Grade:",grades[-1])
print("\tAverage:",old_avg)

new_avg = float(input("What is your desired average:"))
print("Good Luck!",name)
required_marks = round((new_avg-old_avg)*num,2)
print("You will nedd to get a",required_marks,"on your next assignment to earn a",new_avg,"average")

print("\nLet's See What your average could have been if you did better/worse on an assignment.")
grade_change = float(input("What grade would you like to change? :"))
grades.remove(grade_change)
new_grade = float(input("What grade would you like to change " + str(grade_change)+ " to: "))
grades.append(new_grade)

print("New Grades Highest to lowest")
grades.sort(reverse=True)
for grade in grades:
    print("\t",grade)
update_avg = round(sum(grades)/num,2)
print("\n",name,"'s New Grade summary:")
print("\tTotal numbers of Grade:",num)
print("\tHighest Grade:",grades[0])
print("\tLowest Grade:",grades[-1])
print("\tAverage:",update_avg)

print("Your New Average would be a "+str(update_avg)+" Compared to your real average of "+str(old_avg)+" !")
print("That is change of "+str(update_avg-old_avg)+" Points!")

print("Too Bad your original grades are still the Same!")
print(grades)
print("You Should go ask for extra credit!")