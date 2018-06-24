fp=open("read.txt","r")
fp1=open("write.txt","r")
a=fp.readline()
b=fp1.readline()
s=''
while(a!="" and b!=""):
    s+=a+b
    a=fp.readline()
    b=fp1.readline()
print(s)
