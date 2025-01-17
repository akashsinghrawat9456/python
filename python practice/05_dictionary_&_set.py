
    # DICTIONARY AND SET BOTH ARE BROTHERS

        #DICTIONARY
# its a collection of key and value
a={}
print(type(a))
a={
    "harry": "coder sensei",
    "The Hero": "controls online and offline hero"
}
print(a['The Hero'])
print(a)
print(a.get("The Hero"))
a.update({"hero":"normal"})
b={"oreo":"hero's partner"}
a.update(b)
print(a)
print(a.get("oreo"))

            #SET

# its a collection of non-repetive element
        #properties of a set
        #unordered
        #mutable

s=set() # TO DECLARE AN EMPTY SET
n=(3,4,5,6)
s.add(1)# to enter an item in a set
s.add(2) 
print(s)

len(s)# to get the length of a set
s.remove(5) #remove 5 from set s
s.pop(index)# remove the indexed value
# by default 1st index