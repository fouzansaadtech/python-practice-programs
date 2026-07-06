#Count Uppercase and Lowercase Letters 

Char="Python Programming"
upper=0
lower=0
for i in Char:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print("Uppercase Letters = ",upper)
print("Lowercase Letters = ",lower)