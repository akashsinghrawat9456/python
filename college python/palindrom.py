# write a python program to check the palindrome number

a=input("enter the number")
b=int(a)
s=0
n = b
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
    
if s==n:
    print("yes")
else:
    print('not')

