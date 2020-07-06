print("\t\t\tWelcome to the Quadractic Solver App.")
print("""\nA Quadratic equation is of the form ax^2 + bx + c = 0
Your Solutions can be real or complex numbers.
A complex Number has two parts: a+bj
Where a is the real portion and bj is the iamginary portion""")

num = int(input("\nHow many equations would you like to solve today?: "))
for i in range(1,num+1):
    print("\nSolving equation #",i)
    print("----------------------------------------------------------------")
    a = float(input("\nPlease enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    x1 = ((-b+pow(b**2-4*a*c, 0.5))/2*a)
    x2 = ((-b-pow(b**2-4*a*c,0.5))/2*a)
    print("The Solution to "+ str(a)+"x^2 "+" + "+str(b)+"x "+" + "+str(c)+" are:")
    print("\n\tx1 = ",complex(x1))
    print("\tx2 = ",complex(x2))
print("\nThank you for using the Quadratic Solver App.   Goodbye")
