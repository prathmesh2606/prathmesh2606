#Temperature Conversion

#Welcome Msg
print("Welcome to the Temperature Conversion App")

#Gather input from user
Temp_C = float(input("\nWhat is the given Temperature in degree Celsius: "))
Temp_F = (Temp_C)*(9/5) + 32
Temp_K =  Temp_C + 273.15

#Round off upto 4 Decimal
Temp_C = round(Temp_C , 4)
Temp_F = round(Temp_F , 4)
Temp_K = round(Temp_K, 4)

#Displaying Result
print("\nDegrees Celsius : \t\t"+str(Temp_C))
print("Degrees Fahreneheit : \t"+str(Temp_F))
print("Degrees Kelvin : \t\t"+str(Temp_K))
