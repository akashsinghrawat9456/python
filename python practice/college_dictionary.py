dict={}
dict2={1:'apple',2:"ball"}
my_dict={'name':"hero"}
print(dict2)
# nested_dict={dictionary:{translator:"another language"}}
print(dict2[1][2])
dict[1]="grapes"
print(dict2[1][2])
del dict2[1]
print(dict2)
print(len(dict2))
print(my_dict.update(dict2))
print(my_dict)