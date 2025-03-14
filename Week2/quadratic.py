#Inputs
a = 3
b = 1
c = -5

#Equation
x1 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)

print("x1 is",x1,"and x2 is",x2)

#Testing
test1 = a*x1**2 + b*x1 + c
test2 = a*x2**2 + b*x2 + c
if round(test1,5) == 0 and round(test2,5) == 0:
    print("The statement is true")
else:
    print ("The statement is false")