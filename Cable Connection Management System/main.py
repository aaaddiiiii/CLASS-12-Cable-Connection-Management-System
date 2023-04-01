print("\n\n\n\nx=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x\n")
print("Cable Connection Management System v1.1\n")
print("Project Done By : Adithyadev S")
print("                  Alfeen K Afsal")
print("                  Milan G Thomas")
print("                  Muraleemadhavan M")
print("School : SAPS\n")
print("x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")



username=input("\n\nEnter the Admin Username :")       #This Section is For the login page Asking for Username and Password
pswd=input("\nEnter the Admin Password :")
if (username,pswd)!=("",""):
    print("\nEither Username or Password is wrong........\n\nPROGRAM CLOSING........\n")
else:

    print("\nWELCOME.....!")

    import os
    import maintools
    while 1:

        print("\nMAIN MENU...!")
        print("\n1 . Admin Panel")
        print("2 . Customer Reports")
        print("3 . Customer Plans")
        print("4 . Help")
        print("5 . Exit Program\n")
        while True:
            try:
                choice=int(input("Enter your choice as number options : "))
                break
            except ValueError:
                print("\nError : Wrong Input...\n")
        
        if choice==1:
            print("\n1 . Add Customer ID :")
            print("2 . Modify Customer ID :")
            print("3 . Delete Customer ID :")
            print("4 . Back to Main Menu\n")
            while True:
                try:
                    ch=int(input("Enter your choice :"))
                    break
                except ValueError:
                    print("\nError : Wrong input...\n")
            if ch==1:
                maintools.Addcustomer()
            elif ch==2:
                maintools.ModifyCustomer()
            elif ch==3:
                maintools.DeleteCustomer()

        elif choice==2:
            print("\n1. Search Customer ID :")
            print("2. Show Full Customer ID List")
            print("3. Back to Main Menu\n")
            while True:
                try:
                    ch2=int(input("Enter your choice as number : "))
                    break
                except ValueError:
                    print("\nError : Wrong Input...\n")
            if ch2==1:
                maintools.SearchCustomer()
            elif ch2==2:
                maintools.Customerlist()

        elif choice==3:
            maintools.Plans()

        elif choice==4:
            print("\n\n")
            print("=="*86)
            print("\n\nHELP SECTION.........\n\n")
            print("This Software is a Cable Connection Management System, It stores the data of the Customers like the customer name, house number and primary and secondary phone numbers.\nThere are three main sections in this software:-\n\n1. Admin Panel\n2. Customer Reports\n3. Customer Plans\n\n1. Admin Panel lets the admin add, modify or delete a customer ID.\n2. Customer reports lets the admin search for a customer by Name or get the full list of Customers.\n3. The Customer Plans section shows the full customer plan list and then lets the admin modify the plans of the customer.\n\nThis is a simple software and you will get to know it after using for a while...\nThanks You for reffering the help section...")
            print("\n")
            print("=="*86)
            print("\n")

        elif choice==5:
            exit()
