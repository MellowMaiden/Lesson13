#Lesson 13
#Example 1
  #this is how to create a function in Pyhthon
def f(x):
    y=x**2+x+1
    return(y)
#please notice the SPACES under the def, this is because the y is PART OF THE DEFINITION SO SHOULD BE INSIDE IT
#the RETURN means "give the answer back to the user". we can test it because print(f(1)) shoule be 3.
print(f(1))

#Example 2
def F(x):
    y=x**3+2*x**2-x-1
    return(y)
def G(x):
    return(1/x)#you can do both the calculation AND the return in ONE STEP if you want.
print(F(2))
print(G(3))
print(F(G(4)))

#Example 3
def f(x):
    return(x**2)
def g(t):
    return(t**2)
#these are the same function
print(f(3))
print(g(3))

#Example 4
#Example 5
def hypotenuse(a,b):
    c=(a**2+b**2)**0.5
    return(c)
print(hypotenuse(3,4))
print(hypotenuse(5,12))
print(hypotenuse(1,1))

#Example 6
def average(a,b,c):
    x=(a+b+c)/3
    return(x)
print(int(average(6,7,8)))

