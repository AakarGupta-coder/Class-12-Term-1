import csv
#(a)
f=open('student.csv','r')
a=csv.reader(f)
l=[]
for i in a:
    t=tuple(i)
    l.append(t)
print("(A)")
print(l, "\n")

#(b)(i)
f=open('student.csv','r')
a=csv.reader(f)
print("(B)(i)")
for i in a:
    if i[3]<'3':
        print(i[0]+' '+ i[1])
f.close()
print()

#(b)(ii)
f=open('student.csv','r')
a=csv.reader(f)
csee=0
bio=0
mme=0
for i in a:
    if i[4]=='CSEE':
        csee+=1
    elif i[4]=='Biology':
        bio+=1
    elif i[4]=='MME':
        mme+=1
    else:
        continue
print("(B)(ii)")
print(f'No. of people in CSEE department = {csee}')
print(f'No. of people in Biology department = {bio}')
print(f"No. of people in MME department = {mme}")
f.close()
