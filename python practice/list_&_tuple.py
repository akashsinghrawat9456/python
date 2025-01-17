# a=(1,) single tuple
    # In tuple () are used
    
# a=[1,] single list
    # In list [] are used
b=[1,2,3,8,5]
b.sort()
print(b)

b.reverse()
print(b)

b.append(19)
print(b)
b.remove(19)
print(b)
b.insert(4,4) #!! here it just insert in 4th index and nothing is removed
print(b)
b.pop(0) # here index is used
print(b)

    # now tuple turn

a=(1,2,23,45)
print(a.count(2)) # how many 2 are there
print(a.index(23))
