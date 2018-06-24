fp=open("read.txt","r")
#r=str(fp.readlines())
r=fp.readline()
fp1=open("write.txt","w")
while(r!=""):
    fp1.write(r)
    r=fp.readline()
fp1.close()
