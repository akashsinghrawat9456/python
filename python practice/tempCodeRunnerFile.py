a = int(input("Enter the number: "))
temp = a
armstrong_sum = 0

while temp > 0:
    rem = temp % 10
    armstrong_sum += rem ** 3
    temp //= 10

if a == armstrong_sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")
