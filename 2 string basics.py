full_name="           Prathmesh Tapdiya"
print(full_name)
print(full_name.lower()) #gives us lower case string
print(full_name.upper()) #gives us upper case string
print(full_name.title()) #gives us first letter of each string capital
print(full_name.strip()) #removes blank spaces before and after string
full_name =  full_name.title().strip()
print(full_name)

#Escape Character \t & \n
full_name ="\tPrathmesh\nTapdiya"
print(full_name)

message = "Hello buddy!!, How are you? Whats going on?"
print(message)
message= message.lower()
h_count = message.count("h")
print("The Number of h's is " +  str(h_count) +" in a given Message")
#or
print("The number of h's is", h_count, "in a Given Message") 
