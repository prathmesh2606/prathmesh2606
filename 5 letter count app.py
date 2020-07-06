#letter counter app
print("Welcome to the Letter Counter App")

#user input
name = input("\nWhat is your name: ").title().strip()
print("Hello " + name + " ! ")

print("I will Count the Number of times that a Specific letter occurs in a message.")

message = input("\nPlease Enter a message:- ")
letter = input("Which Letter would you like to count the occurrences of:- ")

#standardize to lower case
message= message.lower()
letter=letter.lower()

#Get the count & display results.
letter_count=message.count(letter)
print(name+" your message has "+ str(letter_count) +" "+ letter +" 's in it"+". ") 
