# Count Even and Odd Numbers 

numbers = [10, 15, 22, 35, 40, 51]
even=0
odd=0
for i in numbers:
    if i %2==0:
        even+=1
    else:
        odd+=1
print("Even Numbers:",even)
print("Odd Numbers:",odd)