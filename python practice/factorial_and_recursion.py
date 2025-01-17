def hello():
    print("hello hero")


hello()

n=4
for i in range(n):
    print(i+1)




a=int(input("enter the number"))
def function_by_recursion(a):
    if a==0 or a==1 :
       return 1
    return a * function_by_recursion(a-1)
    
print(function_by_recursion(a))

b=int(input("enter the number"))
def function_by_iteration(b):
    for i in range(b):
        c=(i+1)-b

print(function_by_iteration(b))