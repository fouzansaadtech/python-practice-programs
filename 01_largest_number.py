#Find the Largest Number in a List 

numbers=[25, 18, 90, 45, 12]
lar=numbers[0]
for num in numbers:
    if num>lar:
        lar=num
print("Largest Number =", lar)

