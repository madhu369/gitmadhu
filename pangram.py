import string
l=set(string.ascii_lowercase[:])
s=input().lower().replace(' ','')
if(set(s)==1):
    print('pangram')
else:
    print('not pangram')
