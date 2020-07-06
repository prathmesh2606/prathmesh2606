# Multiplication and Exponent Table App

#Welcome msg
print("Welcome to the Multiplicaton/Exponent Table App")

#gather Information
name = input("\nHello, What is your name: ").title().strip()
num = float(input("What number would you like to work with:- "))
message = name + ", Math is cool!"

#Multiplication Table
print("\nMultiplication Table For "+str(num))
print("\n\t 1.0 * "+ str(num) + " = " + str(round(1*num , 4)))
print("\t 2.0 * "+ str(num) + " = " + str(round(2*num , 4)))
print("\t 3.0 * "+ str(num) + " = " + str(round(3*num , 4)))
print("\t 4.0 * "+ str(num) + " = " + str(round(4*num , 4)))
print("\t 5.0 * "+ str(num) + " = " + str(round(5*num , 4)))
print("\t 6.0 * "+ str(num) + " = " + str(round(6*num , 4)))
print("\t 7.0 * "+ str(num) + " = " + str(round(7*num , 4)))
print("\t 8.0 * "+ str(num) + " = " + str(round(8*num , 4)))
print("\t 9.0 * "+ str(num) + " = " + str(round(9*num , 4)))
print("\t 10.0 * "+ str(num) + " = " + str(round(10*num , 4)))

#Exponential table
print("\nExponential Table For "+str(num))
print("\n\t" + str(num) + " ** 1.0"+ " = "+str(round(num**1, 4)))
print("\t" + str(num) + " ** 2.0"+ " = "+str(round(num**2, 4)))
print("\t" + str(num) + " ** 3.0"+ " = "+str(round(num**3, 4)))
print("\t" + str(num) + " ** 4.0"+ " = "+str(round(num**4, 4)))
print("\t" + str(num) + " ** 5.0"+ " = "+str(round(num**5, 4)))
print("\t" + str(num) + " ** 6.0"+ " = "+str(round(num**6, 4)))
print("\t" + str(num) + " ** 7.0"+ " = "+str(round(num**7, 4)))
print("\t" + str(num) + " ** 8.0"+ " = "+str(round(num**8, 4)))
print("\t" + str(num) + " ** 9.0"+ " = "+str(round(num**9, 4)))
print("\t" + str(num) + " ** 10.0"+ " = "+str(round(num**10, 4)))

#Displaying some message
print("\n",message)
print("\t", message.lower())
print("\t\t", message.title())
print("\t\t\t", message.upper())
