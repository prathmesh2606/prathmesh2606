#Different types of lists program

print("\t\t\tSummary Table")
num_strings = ['15','100','55','42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.1425]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nThe Varible num_strings is a",type(num_strings))
print("It contains the elements: ", num_strings)
print("The Elemnt " + num_strings[0]+ " is a "+ str(type(num_strings[0])))

print("\nThe Variblenum_ints is a",type(num_ints))
print("It contains the elements: ", num_ints)
print("The Elemnt " + str(num_ints[0])+ " is a "+ str(type(num_ints[0])))

print("\nThe Varible num_floats is a",type(num_floats))
print("It contains the elements: ",num_floats)
print("The Elemnt " + str(num_floats[0])+ " is a "+ str(type(num_floats[0])))

print("\nThe Varible num_lists is a",type(num_lists))
print("It contains the elements: ", num_lists)
print("The Elemnt " + str(num_lists[0])+ " is a "+ str(type(num_lists[0])))

#sorting
num_strings.sort()
num_ints.sort()
print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: " , num_strings)
print("Sorted num_ints: " , num_ints)

print("\nStrings are Sorted alphabetically while integers are sorted numerically!")
