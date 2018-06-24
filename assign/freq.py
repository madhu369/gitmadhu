fp=open("read.txt","r")
s=input("enter the word to search")
a=fp.read(len(s))
d=0
count=0
while(a!=""):
    if(s==a):
        count+=1
    d+=1
    fp.seek(d)
    a=fp.read(len(s))
print(count)
fp.close()
