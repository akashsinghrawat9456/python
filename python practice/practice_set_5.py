# #wap to create a dictionary of hindi words with value as their as their english translation provide user with an option to look it up
# hindi={
#         "puch":"ask",
#         "tel":"oil",
#         "de":"give"
#     }
# a=input("enter the hindi word you want to know ")
# print("meaning:",hindi[a])



# wap to input eight numbers from the user and display all the unique numbers(once)

# s2=input("enter the number")
# s3=input("enter the number")
# s4=input("enter the number")
# s5=input("enter the number")
# s6=input("enter the number")
# s7=input("enter the number")
# s8=input("enter the number")
# s9=input("enter the number")

# s={s2,s3,s4,s5,s6,s7,s8,s9}
# print(type(s))
# print(s)


# can we have a set with 18(int) and "18"(str) as a value in it?

# s2=input("enter the number")
# s3=input("enter the string")
# s2=int(s2)
# s={s2,s3}
# print(s)
 
# what will be the length of the following set S:

# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))

# what is the type of s in s={}
# s={}
# print(type(s))

# create an empty dictionary Allow 4 friends to enger their favorite language as value and use keys as their name are unique
# dic={}
# d2=input("enter the number")
# d3=input("enter the number")
# d4=input("enter the number")
# d5=input("enter the number")
# dic['aniket']=d2
# dic ['anikit']=d3
# dic['animesh']=d4
# dic['rachit']=d5
# print(dic)

# if names of 2 friends are same; what will to the program
# dic={}
# d2=input("enter the number")
# d3=input("enter the number")
# d4=input("enter the number")
# d5=input("enter the number")
# dic['aniket']=d2
# dic ['anikit']=d3
# dic['aniket']=d4
# dic['rachit']=d5
# print(dic)

# if name of 2 subject are same; what will to the program
# dic={}
# d2=input("enter the number")
# d3=input("enter the number")
# d4=input("enter the number")
# d5=input("enter the number")
# dic['aniket']=d2
# dic ['anikit']=d3
# dic['animesh']=d4
# dic['rachit']=d5
# print(dic)

 # can you change the values inside a list which contain  in set s
# # s={8,7,12,"hero",[1,2]}
# it will throw error 
# because it is not and don't contain hashable(changable) element(like tuple ,list ,dictionary)
# TypeError: unhashable type: 'list'