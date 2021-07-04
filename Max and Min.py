list = [3,6,2,9,8,2,6,4,1,5,6,8,9]

max=list[3]
min=list[3]
for a in list:
    if a>max:
        max=a
    if a<min:
        min=a
print("min =",min,"max =",max)
