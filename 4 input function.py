#Input function
First_name=input("Enter Your Name:- ")
print("Hello "+ First_name.title())
print("Hello {0}".format(First_name.title())) #.Dot format method
print(f"Hello {First_name.title()}.")

input("Press Enter to Continue!!")
print("Give me two numbers and I'll Multiply them together")
num_1=float(input("Enter the 1st Number:- "))
num_2=float(input("Enter the 2nd Number:- "))
product=num_1*num_2
print("The Product of "+str(num_1)+ " and "+str(num_2)+" is " + str(product) + ".")

input("Press Any Key to Continue!!")
print("Give Me 2 numbers and I'll add them Together")
num_3=float(input("Enter the 1st number:- "))
num_4=float(input("Enter the 2nd number:- "))
Addition=num_3+num_4

print("The Addition of "+str(num_3)+" & "+str(num_4)+" is "+str(Addition)+". ")

#.dot format method for string
print("The Addition of {0} & {1} is {2}.".format(num_3,num_4,Addition) )

# print using f-strings
print(f"The Addition of {num_3} & {num_4} is {Addition}.")
