import csv
#(a)
f=open('placement.csv','r')
r=csv.reader(f)
print('(a) The placement.csv contains the following:')
for i in (r):
    if r.line_num==0:
        continue
    else:
        print(i)

#(b)
def count():
    f=open('placement.csv','r')
    r=csv.reader(f)
    for i in (r):
        r.line_num
    print(f'\n(b) Total no. of candidates that came for placement test are {r.line_num-1}.')

#(c)
def function(k):
    return int(k[7])
def topper():
    f=open('placement.csv','r')
    r=csv.reader(f)
    l=[]
    for i in r:
        if r.line_num==1:
            continue
        else:
            s=int(i[-1])+int(i[-2])+int(i[-3])+int(i[-4])+int(i[-5])
            i.append(s)
            l.append(i)
    l.sort(key=function,reverse=True)
    n=int(input('\n(c) Enter the no. of top candidates required: '))
    print('Top',n,'candidates are: ')
    for i in range(n):
        print(f'{i+1}. {l[i]}')
count()
topper()
