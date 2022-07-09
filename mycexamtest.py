class library:
    i=0
    def __init__(self,vardhan):
        self.vardhan=vardhan
    def avaliablebooks(self):
        print("The books we have in our library are as follows:")
        for i in self.vardhan:
            print(i)
    def typesofbooks(self):
        print("HEY HII THERE")
        print("The type of books we have are:")
        print("""1.HISTORY
                 2.SCIENCE
                 3.CRIMES
                 4.MATHS
                 5.WORLD WAR
                 6.ECONOMICS""")
    def departments(self):
        print("""1.shelf 1 
                 2.shelf 2
                 3.shelf 3
                 4.shelf 4""")
    def givingbooks(self,requestedbook):
        if requestedbook in self.vardhan:
            print("Hey the book you requested is Borrowed")
            self.vardhan.remove(requestedbook)
        else:
            print("SORRY THE BOOK YOU REQUESTED IS NOT PRESENT IN OUR LIBRARY")
    def adding(self,returnb):
        self.vardhan.append(returnb)
        print("THANKS FOR RETURNING THE BOOK")
class student:
    def requestbook(self):
        print("Hey hi PLEASE request the books that are avaliable only")
        print("Enter the book you want to request")
        self.name=input()
        return self.name
    def returnbook(self):
        print("ENTER THE NAME OF THE BOOK YOU WANT TO ENTER")
        self.v1=input()
        return self.v1
class vishnu():
    def nakka(self):
        print("enter name")
        self.name=input()
        print("enter phone number")
        self.phone=int(input())
        print("enter mail")
        self.mail=input()
        print("enter password")
        self.password=input()
        print("good you have registered")
    def update(self):
        print("do you want to update your details if yes please enter y else n")
        n=input()
        if(n=='y'):
            print("please update your name")
            self.name=input()
            print("please update phone num")
            self.phone=int(input())
            print("please update your mail")
            self.mail=input()
            print("please update your password")
            self.password=input()

v=library(["THE FIGHTER","THE MAD MEN","GOT","CRIME","INTERSHALA","VISHNU THE AWESOME","NOBODY","KILLER"])
stu=student()
bb=vishnu()
print("-----------------welcome to Vishnu Library----------------")
for i in range(1,9):
    print(""" Choice the option you want
            1.Display all the avaliable books
            2.See the types of books Avaliable
            3.Various Departments1
            4.Request a Book
            5.Return a Book
            6.Sign up for Library MEMBERSHIP
            7.Update signup MEMBERSHIP
            8.Exit """)
    print("please enter your choice")
    ch=int(input())
    if(ch==1):
        v.avaliablebooks()
    elif(ch==2):
        v.typesofbooks()
    elif(ch==3):
        v.departments()
    elif(ch==4):
        v.givingbooks(stu.requestbook())
    elif(ch==5):
        v.adding(stu.returnbook())
    elif(ch==6):
       bb.nakka()
    elif(ch==7):
        bb.update()
    else:
        exit()

    