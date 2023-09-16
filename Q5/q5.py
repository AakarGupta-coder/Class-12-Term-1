import pickle
# (a)
def write():
    f=open('hotel.dat','ab')
    print("\n(a)")
    d={}
    d['roomno.']=int(input("Enter your Room Number: "))
    d['name']=input("Enter your name: ")
    d['duration']=int(input("Enter the number of days you stayed: "))
    pickle.dump(d,f)
    f.close()
# (b)
def read():
    f=open("hotel.dat","rb")
    print("\n(b) Details of customers:-")
    while True:
        try:
            d=pickle.load(f)
            print(d)
        except EOFError:
            f.close()
            break
# (c)
def count():
    c=0
    f=open("hotel.dat",'rb')
    while True:
        try:
            pickle.load(f)
            c=c+1
        except EOFError:
            f.close()
            break
    print(f"\n(c) {c}")
# (d)
def customer():
     f=open("hotel.dat","rb")
     print("\n(d) Customers who stayed for more than 2 days are: ")
     while True:
          try:
            d=pickle.load(f)
            if d['duration']>2:
                  print(d)
          except EOFError:  
            f.close()
            break
def menu():
    while True:
        print("\n1. Enter the details of the customer.")
        print("2. Display the details of the customer.")
        print("3. Count the number of customers.")
        print("4. Customers who have stayed in the hotel for more than 2 days.")
        print("5. Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            write()
        elif ch==2:
            read()
        elif ch==3:
            count()
        elif ch==4:
            customer()
        elif ch==5:
            print("\nProgram Ended Successfully.")
            break
        else:
            print("Invalid Choice!")
menu()
