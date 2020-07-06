import math
print("\t\t\tWelcome to Factorial Calculator App")
num = int(input("What number would you like to compute the factorial of ?: "))
print(str(num) + "! =",end = " ")
for i in range(1,num):
    print(str(i)+"*",end="")
print(num)

ans = math.factorial(num)
print("\nHere is the result from math library: ")
print("The Factorial of "+str(num)+" is "+str(ans)+".")

mul = 1
for i in range(1,num+1):
    mul *= i
print("\nHere is the result from my own algorithm: ")
print("The Factorial of "+str(num)+" is "+str(mul)+".")
