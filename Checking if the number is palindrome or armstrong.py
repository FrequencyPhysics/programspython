#04/07/2021

num = int(input("Enter a number: "))

sum = 0

reverse = 0

temp = num

temp1 = num

while num > 0:
    digit = num % 10
    sum = sum* 10 + digit
    num = num // 10
while  temp1> 0:
    d = temp1 % 10
    reverse = d*d*d + reverse
    temp1 =temp1//10


if temp == sum:
    print(temp,"is a palindrome")
else:
    print(temp,"is not a palindrome")
if  temp == reverse:
    print(temp, "is an Armstrong number")
else:
    print(temp,"is not an Armstrong number.")
