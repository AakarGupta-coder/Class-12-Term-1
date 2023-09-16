def isvowel():
    f1=open('file1.txt','r')
    l=f1.readlines()
    f2=open('file2.txt','w')
    vowel='aeiou'
    for i in l:
        s=i.strip("\n")
        n=s.split()
        for j in n:
            if j[0] not in vowel and j[0] not in vowel.upper():
                f2.write(j+" ")
    f1.close()
    f2.close()
    print("Task Successfully Completed!")
isvowel()
