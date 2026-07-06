# Reverse a String Without Using Slicing 

n="Python"
v=""
rev=len(n)-1

while rev>=0:
    v+=n[rev]
    rev-=1
print(v)
