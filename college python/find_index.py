# Write a Python program to find the index of an item in a specified list.
a=input("enter the element")
b=input("enter the element")
d=input("enter the element")
e=input("enter the element")
c=[a,b,d,e]
f=input("enter the number of which you want index")
if f in c:
    index = c.index(f)
    print("Index of", f, "is", index)
else:
    print(f, "is not present in the list.")