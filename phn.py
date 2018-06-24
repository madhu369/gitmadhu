import re
num=input()
pattern = r'^(\+91-)[6789](\d){9}'
if re.match(pattern,num):
    print('true')
else:
    print('false')
