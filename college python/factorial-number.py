def factorial(fact):
    if fact==0:
        return 1
    else :
        return fact* factorial(fact-1)
fact=int(input("enter the element"))
print("factorial of",fact,"is",factorial(fact))
