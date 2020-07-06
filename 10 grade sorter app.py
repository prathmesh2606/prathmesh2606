#Grade Sorter App
print("\t\t\tWelcome to the Grade Sorter App")

#user input
grades = []
grades.append(int(input("\nWhat is Your first Grade (0-100): ")))
grades.append(int(input("What is Your 2nd Grade (0-100): ")))
grades.append(int(input("What is Your 3rd Grade (0-100): ")))
grades.append(int(input("What is Your 5th Grade (0-100): ")))

print("\nYour Grades are: ",grades)

#sorting from high to low
grades.sort(reverse=True)
print("\nYour Grades from hoghest to lowest are: ",grades)

#dropping lowest value
print("\nThe Lowest two grades will now be dropped.")
remove_1 = grades.pop()
print("Removed Grade:",remove_1)
remove_2 = grades.pop(-1)
print("Removed Grade:",remove_2)

#displaying final Results
print("\nYour remaining grades are: ",grades)
print("Nice Work !  Your Highest grade is a ",grades[0])
