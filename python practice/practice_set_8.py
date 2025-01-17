# # write a program using function to find the greatest of the three number
# b=int(input("enter the number"))
# a=int(input("enter the number"))
# c=int(input("enter the number"))

# def hero(a,b,c):
#     if a>b and a>c:
#         print(a,"is the greatest among them")
#     elif c>a and c>b:
#         print(c,"is the greatest among them")
#     elif b>a and b>c:
#         print(b,"is the greatest among them")
#     else:
#         print("ALL ARE EQUAL")
# hero(a,b,c)

# write a  python program by using function to convert celcius to fahrenheit
# a=int(input("enter the celcius:"))

# def converter(a):
#     f=a*(9/5)+32
#     print("fahrenheit=",f)
# converter(a)

# how to prevent a python print() function to print a new line at the end

# print("hero",end="")
# print("hero",end="")
# print("hero",end="")

# write a iterative function to calculate the sum of the first n natural numbers
# n=int(input("enter the number"))
# def summ(n):
#     p=0
#     for i in range(n):
#         i+=1
#         p+=i
#     print("sum of the natural number=",p)
# summ(n)

# write a recursive function to calculate the sum of the first n natural numbers

# def som(n):
#     if n==1:
#         return 1
#     else:
#         return som(n-1)+n
# n=int(input("enter the number"))
# print(som(n))

# write a python function to print first n lines of the following pattern
# n=3
# ***
# **
# *
# n=int(input("enter the number"))
# def star(n):
#     for i in range (n) :
#         print("*" * n)
#         n-=1
# star(n)


# # write a python function which converts inches to cms
# def con(n):
#     print(n*2.54,"cm")
# n=int(input("enter the value in inches"))
# con(n)

# write  a python function to remove a given a word from a string and strip it at the same time
# def h(n,w):
#     m=n.replace(w, "")
#     return m.strip()
    
# n=input("enter the string")
# w=input("enter the word")
# g= h(n,w)
# print(g)
# write a python function to print the multiplication table
# def table(n):
#     for i in range (10):
#        i+=1
#        print(n,"*",i,"=",n*i) 
# n=int(input("enter the number"))
# table(n)
