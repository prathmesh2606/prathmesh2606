#Favorite Teachers Program

#welcome msg
print("\t\t\tWelcome to the Favorite Teachers Program")

#Gather input from user and put it into list
teacher = []
teacher.append(input("\nWho is your first favorite teacher: ").title().strip())
teacher.append(input("Who is your second favorite teacher: ").title().strip())
teacher.append(input("Who is your third favorite teacher: ").title().strip())
teacher.append(input("Who is your forth favorite teacher: ").title().strip())

#Displaying, sorting the list
print("\nYour favorite teachers ranked are: ",teacher)
print("Your favorite teachers ranked are: ", sorted(teacher))
print("Your favorite in reverse alphabetical order are: ",sorted(teacher, reverse = True))

print("\nYour top two teachers are: " + teacher[0] + " and " + teacher[1]+".")
print("Your next two favorite teachers are: " + teacher[2] + " and " + teacher[3]+".")
print("Your last favorite teacher is: " + teacher[3] + ".")
print("Your have a total of : " + str(len(teacher)) + " favorite teachers.")

#adding new teacher
print("\nOops, "+teacher[0]+" is no long your first favorite teacher."  ,end = " ")
new_teacher = input("Who is your new FAVORITE Teacher? : ")
teacher.insert(0 , new_teacher)

#Again Displaying, sorting the updated list
print("\nYour favorite teachers ranked are: ",teacher)
print("Your favorite teachers ranked are: ", sorted(teacher))
print("Your favorite in reverse alphabetical order are: ",sorted(teacher, reverse = True))

print("\nYour top two teachers are: " + teacher[0] + " and " + teacher[1]+".")
print("Your next two favorite teachers are: " + teacher[2] + " and " + teacher[3]+".")
print("Your last favorite teacher is: " + teacher[3] + ".")
print("Your have a total of : " + str(len(teacher)) + " favorite teachers.")

#removing teacher from list
print("You've Decided you no loger like a teacher.", end =" ")
remove = input("Which Teacher would you like to remove from your list? : ").title().strip()
teacher.remove(remove)

#Again Displaying, sorting the updated list
print("\nYour favorite teachers ranked are: ",teacher)
print("Your favorite teachers ranked are: ", sorted(teacher))
print("Your favorite in reverse alphabetical order are: ",sorted(teacher, reverse = True))

print("\nYour top two teachers are: " + teacher[0] + " and " + teacher[1]+".")
print("Your next two favorite teachers are: " + teacher[2] + " and " + teacher[3]+".")
print("Your last favorite teacher is: " + teacher[3] + ".")
print("Your have a total of : " + str(len(teacher)) + " favorite teachers.")
