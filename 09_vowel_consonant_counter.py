#Check Whether a Character is a Vowel or Consonant 

n=input("Letter:")
n1=["A","E","I","O","U"]
n2=["a","e","i","o","u"]
if n in n1 or n in n2:
    print(n,"is a Vowel.")
else:
    print(n,"is a Consonant.")