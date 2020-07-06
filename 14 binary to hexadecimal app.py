#For loops challenge 11: Binary Hexadecimal converter app
print("\t\t\tWelcome to the Binary/Heaxadecimal converter App")

#Get user input and generate lists.
max_value = int(input("\nCompute binary and Hexadecimal values up to the following decimal number:"))
decimal = list(range(1, max_value+1))
binary = []
hexadecimal = []
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Genrating lsits.......Complete!")

#Get slicing index from user.
print("\nUsing slices, we will now show a portion of each list.")
lower_range = int(input("What decimal nuber would you like to start at: "))
upper_range = int(input("What decimal nuber would you like to stop at: "))

#slice through each list individually
print("\nDecimal values from"+str(lower_range)+" to "+str(upper_range)+ ":")
for num in decimal[lower_range-1:upper_range]:
    print(num)

print("\nBinary values from"+str(lower_range)+" to "+str(upper_range)+ ":")
for num in binary[lower_range-1:upper_range]:
    print(num)

print("\nHexadecimal values from"+str(lower_range)+" to "+str(upper_range)+ ":")
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)

#output the whole list to the screen
input("\nPress Enter to see all values from 1 to"+str(max_value)+" .")
print("Decimal-----Binary-----Hexadecimal")
print("------------------------------------------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d)+ "----" + str(b)+ "-----"+str(h))
