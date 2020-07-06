#Grocery list App
import datetime 
time = datetime.datetime.now()
#welcome Screen
print("\t\t\tWelcome to the Grocery List App.")
print("Current Date and Time: ",time)

grocery = ["Meat", "Cheese"]
print("You currently have Meat and Cheese in your list.")

#Input from users
grocery.append(input("\nType of food to add to the grocery list: ").title().strip())
grocery.append(input("Type of food to add to the grocery list: ").title().strip())
grocery.append(input("Type of food to add to the grocery list: ").title().strip())
print("\nHere is your grocery list:\n", grocery)

#sorting
grocery.sort()
print("Here is your grocery list sorted:\n", grocery)

#Msg Display
print("\nSimulating grocery shopping...")

#Removing from list
print("\nCurrent grocery list: " + str(len(grocery)) + " items" + "\n" + str(grocery))
remove = input("What food did you  jsut buy: ").title().strip()
grocery.remove(remove)
print("Removing " + remove + " from list....")

print("\nCurrent grocery list: " + str(len(grocery)) + " items" + "\n" + str(grocery))
remove = input("What food did you  jsut buy: ").title().strip()
grocery.remove(remove)
print("Removing " + remove + " from list....")

print("\nCurrent grocery list: " + str(len(grocery)) + " items" + "\n" + str(grocery))
remove = input("What food did you  jsut buy: ").title().strip()
grocery.remove(remove)
print("Removing " + remove + " from list....")

#Displaying updated list after removing
print("\nCurrent grocery list: " + str(len(grocery)) + " items" + "\n" + str(grocery))

#meat out of stock
grocery.remove("Meat")
print("\nSorry, the store is out of Meat.")

#Adding other material insted of meat
grocery.append(input("What food would you like instead: ").title().strip())

#Displaying final list
print("\nHere is what remains on your grocery list:\n", grocery)
