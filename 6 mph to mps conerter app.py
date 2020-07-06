#MPH to MPS conversion app

#Welcom screen message
print("Welcome to the MPH to MPS Conversion App")

#taking input from user
MPH = float(input("\nWhat is your Speed in Miles Per Hour (MPH) : "))

#Calculation
MPS= 0.4470389*MPH
MPS= round(MPS, 2)

#Printing Result
print("Your Speed in Meters Per Second (MPS) is: ",MPS)
#or
#print("Your Speed in MPS is: "+str(MPS)+" .")
