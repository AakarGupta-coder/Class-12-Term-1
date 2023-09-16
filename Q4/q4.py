f=open('myfile.txt','r')
r=f.read()
#(A)
a=r.split()
d={}
for i in a:
    if i.lower() not in d:
        d[i.lower()]=1
    else:
        d[i.lower()]+=1
print("(A)")
print(d)
print('(i) Total no. of words are:',len(a))
print('(ii) No. of different words are:',len(d))
x=0
for i in d:
    if d[i]>x:
        x=d[i]

for i in d:
    if d[i]==x:
        print(f'(iii) The most common words in the file is: "{i}"')

#(B)(i)

d2={}
for i in d:
    if len(i) not in d2:
        d2[len(i)]=[i]
    else:
        d2[len(i)].append(i)
print('\n\n(B)(i)',d2)

#(B)(ii)
def find_longest_word():
    n=0
    for i in d2:
        if i>n:
            n=i
    for i in d2:
        if i==n:
            print(f'(ii) The longest words in the file are {d2[i]}')

#(B)(iii)
def filter_long_words(n):
    l=[]
    for i in d2:
        if i>n:
            l.extend(d2[i])
    print(f'The list of words that are longer than {n} are:',l)

find_longest_word()
m=int(input('(iii) Enter the no. of letters to check for: '))
filter_long_words(m)
