a=[3,1,2,4,1,2,3]
b=[]
c=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            b.append(j-i)
            c=c+1
b.sort()
print(b[0])
