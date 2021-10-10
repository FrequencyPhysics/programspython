#Write a program to find the sum of the array

a = []
a = [1,2,3,4,5]

ans = sum(a)
print("sum of array is: ", ans)
#Write a program to find the largest number of the array
max = a[0]

for i in range(0, len(a)):

    if (a[i] > max):
        max = a[i]

print("Largest number in array: " + str(max))



#Write a python program for find remainder of array multiplication divided by n

def findremainder(h, lens, n):
    mul = 1
    for i in range(lens):
        mul = (mul * (h[i] % n)) % n
    return mul % n

h = [100, 1, 2, 3, 4, 5, 6, 6, 7]
lens = len(h)
n = 11
print(findremainder(h, lens, n))


# Check if given array is Monotonic
def isMonotonic(A):

	return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
			all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


A = [6, 5, 4, 4]


print(isMonotonic(A))
