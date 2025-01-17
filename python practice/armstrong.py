# a= int(input("enter the number"))
# temp=a
# sum=0
# while temp>0:
#     rem=temp%10
#     sum+= rem ** 3
#     temp//=10
#     if a==sum:
#         print("armstrong")
#     else:
#         print("not armstrong")


a = int(input("Enter the number: "))
temp = a
armstrong_sum = 0

while temp > 0:
    rem = temp % 10
    armstrong_sum += rem ** 3
    temp //= 10
if a == armstrong_sum:
    print(a"Armstrong number")
else:
    print(a"Not Armstrong number")
