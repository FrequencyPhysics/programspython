# 03/07/2021

x = 6523
count_x = 0

def reverse(x):
    global count_x
    if x > 0:
        xy = x % 10
        count_x = (count_x * 10) + xy
        reverse(x //10)
    return count_x


count_x = reverse(x)

print("Reversed number is: " , count_x)
