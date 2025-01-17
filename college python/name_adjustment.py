# name='oreo';
# print("original String is",name)
# res=name[0]
# len=len(name)
# middle=int(len/2)
# res=res+name[middle]
# res=res+name[len-1]
# print("new String",res)


# # wap to create a string made of the first, middle and last character

# def extract_characters(s):
#     if len(s) == 0:
#         return ""  # Return an empty string if input is empty
#     elif len(s) < 3:
#         return s  # Return the string itself if it is too short
#     else:
#         first_char = s[0]
#         middle_char = s[len(s) // 2]
#         last_char = s[-1]
#         return first_char + middle_char + last_char

# # Example usage
# input_string = input("Enter a string: ")
# result = extract_characters(input_string)
# print("Resulting string:", result)



def m3c(s):
    if len<3:
        print("string is too short")
    elif len % 2==0:
        print("string must be odd")
    else:
         m = len//2
    return m3c[m-1:m+2]

s= input("enter a string:")
result=m3c(s)
print("middle three characters:",result)
