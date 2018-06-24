'''import math
x=int(input("enter the number1"))
y=int(input("enter the number2"))
s=math.gcd(x,y)
print(s)'''

l=[]
x=int(input("enter the number1"))
y=int(input("enter the number2"))
if(x>y):
    n=x
else:
    n=y
for i in range(1,n):
    if(x%i==0 | y%i==0):
        l.append(i)
l.sort()
s=len(l)-1
print(l[s])
