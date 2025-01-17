# # write a program to print the table of a given number by using for loop
# a=int(input("enter the number"))
# for i in range(1,11):
#     print(a,"*",i,"=",a*i)


# write a program to greet all the person names stored in a list l1 and which starts with 5

# l1=["Harry","Sohan","Sachin","Rahul"]
# for a in l1:
#     print(a)


# # write a program to print the table of a given number by using while loop
# a=int(input("enter the number"))
# i=1
# while i<11:
#   print(a,"*",i,"=",a*i)
#   i+=1


# # write  a program to find whether a given number is prime or not
# c=0
# a=int(input("enter the number"))
# for i in range (1,a+1):
#     if a%i==0:
#         c+=1

# if c<=2:
#     print("prime")
# else:
#     print("composite")
        
# write a program to find  the sum of first n natural numbers using while loop
# i=1
# sum =0
# a=int(input("enter the number"))
# while i<=a:
#     sum +=i
#     i +=1   
# print(sum)
# i = 1
# sum = 0
# a = int(input("Enter the number: "))
# while i <= a:
#     sum += i
#     i += 1

# print("Sum of the first", a, "natural numbers is:", sum)

# write a program to calculate the factorial of a given number using for loop
# a=int(input("enter the number"))
# sum=0
# if a==0:
#         print("factorial=1")
# else :
#     for i in range (1,a+1):
#         sum+=i
#     print("factorial=",sum)

# write a program to print the following star pattern 
# *
# **
# ***

# i=1
# a=int(input("enter the number"))
# for i in range (a+1):
#     print("x"*i)

# write a program to print the following star pattern:
#   +           
#  +++
# +++++


# a=int(input("enter the number"))
# for i in range (a):
#     print(" "*(a-i-1),end="")
#     print("*"*(2*i+1),end="")
#     print(" "*(a-i-1))

# write a program to print the following star pattern/
# xxxxxxxxxxxx
# x          x
# x          x
# x          x
# x          x
# x          x
# x          x
# x          x
# x          x
# xxxxxxxxxxxx
# a=int(input("enter the number"))

# for i in range(a):
#     if i==0:
#         print("x"*a)
#     elif i==(a-1):
#         print("x"*a)
#     else:
#         print("x"," "*(a-4),"x")

# write a program to print multiplicaation table of n using for loop in reversed order
# a=int(input("enter the number:"))
# print("\n\t table of ",a)
# n=10
# print("\n")
# for i in range(10):
#     print(a,"*",n,"=",a*n)
#     n-=1