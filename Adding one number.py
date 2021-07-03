# 03/07/2021


num = int(input("Enter a number: "))
result = 0

while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num / 10)

print("Sum of all digits is: ", result)
