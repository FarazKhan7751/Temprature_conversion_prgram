class contact:
    def __init__(self):
        self.main_lst=[]
        self.sub_lst=[]
    def add_contact(self):
        name=str(input("Enter name = "))
        email=str(input("Enter your Email address = "))
        phone=str(input("Enter phone number = "))
        self.sub_lst.append(name)
        self.sub_lst.append(email)
        self.sub_lst.append(phone)
        self.main_lst.append(self.sub_lst)
        print("your contact is successfully added")
    def edit_contact(self):
        print("press 1 if you want to change name")
        print("press 2 if you want to change email")
        print("press 3 if you want to chnage phone number")
        change=int(input("Enter your choice = "))
        if(change==1):
            email=str(input("Enter your email = "))
            phone=str(input("Enter your phone number = "))
            for i in range(len(self.main_lst)):
                if (self.main_lst[i][1]==email and self.main_lst[i][2])==phone:
                    name=str(input("Enter the changed name = "))
                    self.main_lst[i][0]=name
                    print("your name change successfully")
        elif(change==2):
            name=str(input("Enter your name = "))
            phone=str(input("Enter your phone number = "))
            for i in range(len(self.main_lst)):
                if (self.main_lst[i][0]==name and self.main_lst[i][2])==phone:
                    email=str(input("Enter the changed email = "))
                    self.main_lst[i][1]=email
                    print("your Email change sussessfully ")
        elif(change==3):
            name=str(input("Enter your name = "))
            email=str(input("Enter your email = "))
            for i in range(len(self.main_lst)):
                if (self.main_lst[i][0]==name and self.main_lst[i][1])==email:
                    phone=str(input("Enter the changed phone number = "))
                    self.main_lst[i][1]=phone
                    print("your phone number changed sussfully")
        else:
            print("Enter correct information")
    def view_contact(self):
        for i in self.main_lst:
            print(i,"/n")
            
obj=contact()
print("Press 1 to add a contact")
print("Press 2 to update a contact")
print("Press 3 to view a contact")
print("press 4 to exit the programm")
choice=int(input("Enter your choice = "))
if choice==1:
    obj.add_contact()
elif choice ==2:
    obj.edit_contact()
elif choice==3:
    obj.view_contact()
elif choice==4:
    print("Exiting program")
else:
    print("Enter correct information")
