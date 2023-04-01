import os                                                                    #calling modules
import string


def Addcustomer():                                                           #function to add customer details
    name=input("\nEnter the Customer Name (Max 14 Charecters)   : ")         #input section
    add=input("Enter the House Number                        : ")            #string.capwords(x) is used to make the first alphabet of the name capital and all other small
    ph1=input("Enter the Phone number 1                      : ")
    ph2=input("Enter the Phone Number 2                      : ")
    file = open("customer.txt", "a")
    data=string.capwords(name)+","+add+","+ph1+","+ph2+"\n"
    file.write(data)
    file.close()
    print("\nNew Customer ID added\n")
    
    file2=open("customer_plan.txt","a")                                      #subsection which inputs the customer plan also
    while True:
        try:
            inp=input("Do you want to activate the plan for this Customer ? (y / n) :")
            if inp=="n":
                status="DEACTIVATED" 
                plan="________"
                bill="________"
                print("\nPlan kept nil !")
            elif inp=="y":
                plano=input("\nEnter the plan the customer want \n\n1. Normal Plan (Rs 350 / month)\n2. Supreme HD Plan (Rs 650 / month)\n\nEnter input as 1 or 2 : ")
                status="ACTIVATED"
                if plano=="1":
                    plan="Normal Plan"
                    bill="350"
                elif plano=="2":
                    plan="HD Plan"
                    bill="650"
                    print("\nPlan added for this Customer !")
            data2=string.capwords(name)+","+status+","+plan+","+bill+"\n"
            file2.write(data2)
            file2.close()
            break
        except UnboundLocalError:
            print("\nError : Wrong Input...\n")
    
        
def ModifyCustomer():                                                        #function to modify customer details


    filist=open('customer.txt','r')                                          #this section shows the customer list
    print("\n\n")
    for i in range(44):
        print("==",end="")
    print("\n\nCustomer Name \t\t House Number \t\t Phone No. 1 \t\t Phone No. 2 \n")  
    for i in range(44):
        print("==",end="")
    print("\n")
    for rox in filist:
        name,Address,ph1,ph2=rox.split(',')
        print(name,"\t\t",Address,"\t\t",ph1,"\t\t",ph2)
    filist.close()
    for i in range(44):
        print("==",end="")
    print("\n")

    found=0
    print("\nModification Panel\n")
    sname=input("Enter the Name to Search : ")
    filein=open('customer.txt','r+')
    for row in filein:
        name,add,ph1,ph2=row.split(',')
        if (name.lower()).strip()==(sname.lower()).strip():                  #name.lower() is used to avoid the error due to capital and small letter error
            print("\n")
            print("=="*20)
            print("\nCustomer Name    : ",name)
            print("House Number     : ",add)
            print("Phone Number 1   : ",ph1)
            print("Phone Number 2   : ",ph2)
            print("=="*20)
            found=1
            break
    if (found==0):
        print("\nEntered Name was not found in the Customer list......")
        filein.close()
    elif (found==1):
        filein=open('customer.txt','r+')                                     #this section actually modify the details in customer.txt (customer details)
        fileout=open('sample_customer.txt','w+',newline='')
        for row in filein:
            name,add,ph1,ph2=row.split(',')
            if (name.lower())==(sname.lower()):
                nameX=input("\n\nEnter the new Name       : ")
                add=input("Enter the House Number   : ")
                ph1=input("Enter the Phone Number 1 : ")
                ph2=input("Enter the Phone Number 2 : ")
                data=string.capwords(nameX)+","+add+","+ph1+","+ph2+"\n"
                fileout.write(data)
            else:
                fileout.write(row)
        filein.close()
        fileout.close()
        os.remove("customer.txt")
        os.rename("sample_customer.txt","customer.txt")

    found2=0                                                                #checks for the name is customer_plan.txt
    filein2=open('customer_plan.txt','r+')
    for row2 in filein2:
        name2,status,plan,bill=row2.split(',')
        if (name2.lower()).strip()==(sname.lower()).strip():
            found2=1
            break

    if (found2==0):
        print("\nThere was some problem with the Program....")
        filein2.close()
    elif (found2==1):                                                       #modifying customer_plan.txt
        filein3=open('customer_plan.txt','r+')                                     
        fileout3=open('sample_customer_plan.txt','w+',newline='')
        for row3 in filein3:
            name,status,plan,bill=row3.split(',')
            if (name.lower())==(sname.lower()):
                data3=string.capwords(nameX)+","+status+","+plan+","+bill
                fileout3.write(data3)
            else:
                fileout3.write(row3)
        filein3.close()
        fileout3.close()
        os.remove("customer_plan.txt")
        os.rename("sample_customer_plan.txt","customer_plan.txt")    
        
def SearchCustomer():                                                        #function to search for customer name
    kfound=0
    sname=input("\nEnter the Name to Search : ")
    filein=open('customer.txt','r+')
    for row in filein:                                         
        name,add,ph1,ph2=row.split(',')
        if (name.lower()).strip()==(sname.lower()).strip():                  #name.lower() is used to get rid of the error due to capital letter               
            kfound=1
            print("\n")
            print("=="*20) 
            print("\nCustomer Name    : ",name)
            print("House Number     : ",add)
            print("Phone Number 1   : ",ph1)
            print("Phone Number 2   : ",ph2)
            print("=="*20)

    if (kfound==0):
        print("\nEntered name was not found in the list...!")

def Customerlist():                                                          #function to show full customer list
    filein=open('customer.txt','r')
    print("\n\n")
    for i in range(44):
        print("==",end="")
    print("\n\nCustomer Name \t\t House Number \t\t Phone No. 1 \t\t Phone No. 2 \n")  
    for i in range(44):
        print("==",end="")
    print("\n")
    for row in filein:
        name,Address,ph1,ph2=row.split(',')
        print(name,"\t\t",Address,"\t\t",ph1,"\t\t",ph2)
    filein.close()
    for i in range(44):
        print("==",end="")
    print("\n")

def DeleteCustomer():                                                        #function to delete customer ID

    filein=open('customer.txt','r')                                          #this section shows the full customer list
    print("\n\n")
    for i in range(44):
        print("==",end="")
    print("\n\nCustomer Name \t\t House Number \t\t Phone No. 1 \t\t Phone No. 2 \n")  
    for i in range(44):
        print("==",end="")
    print("\n")
    for row in filein:
        name,Address,ph1,ph2=row.split(',')
        print(name,"\t\t",Address,"\t\t",ph1,"\t\t",ph2)
    filein.close()
    for i in range(44):
        print("==",end="")
    print("\n")
    
    found=0                                                           #input name
    print("\nDELETE PANEL....!")
    filein=open('customer.txt','r+')
    sname=input("\nEnter the Name to search : ")
    for row in filein:
        name,add,ph1,ph2=row.split(',')
        if (name.lower()).strip()==(sname.lower()).strip():
            print("\n")
            print("=="*20)
            print("\nCustomer Name            : ",name)
            print("Customer House Number    : ",add)
            print("Customer Phone Number 1  : ",ph1)
            print("Customer Phone Number 2  : ",ph2)
            print("=="*20)
            found=1
            break
    if(found==0):
        print("\nEntered Name not found in search ! ")
        filein.close()
    else:
        filein=open('customer.txt','r+')                                  #deleting ID in customer.txt
        fileout=open('sample_customer.txt','w+',newline='')
        for row in filein:
            name,add,ph1,ph2=row.split(',')
            if (name.lower()==sname.lower()):
                pass
            else:
                fileout.write(row)
        filein.close()
        fileout.close()
        os.remove("customer.txt")
        os.rename("sample_customer.txt","customer.txt")

    found=0
    filein=open('customer_plan.txt','r+')
    for row in filein:
        name,status,plan,bill=row.split(',')
        if (name.lower()).strip()==(sname.lower()).strip():
            found=1
            break
    if(found==0):
        print("\nProgram Malfunction...! ")
        filein.close()
    else:
        filein=open('customer_plan.txt','r+')                             #deleting ID from sample_customer_plan.txt
        fileout=open('sample_customer_plan.txt','w+',newline='')
        for row in filein:
            name,status,plan,bill=row.split(',')
            if (name.lower()==sname.lower()):
                pass
            else:
                fileout.write(row)
        filein.close()
        fileout.close()
        os.remove("customer_plan.txt")
        os.rename("sample_customer_plan.txt","customer_plan.txt")
        print("\nDELETION SUCCESSFUL.....!!")


def Plans():                                                             #function to modify customer plans

    filein=open('customer_plan.txt','r')                                 #this section shows the full customer plan list
    print("\n\n")
    for i in range(43):
        print("==",end="")
    print("\n\nCustomer Name \t\t Status \t\t Customer Plan \t\t Amount Paid \n")  
    for i in range(43):
        print("==",end="")
    print("\n\n")
    for row in filein:
        name,status,plan,bill=row.split(',')
        print(name,"\t\t",status,"\t\t",plan,"\t\t",bill)
    filein.close()
    for i in range(43):
        print("==",end="")
    print("\n")

    changes=input("\nDo you want to make any changes to any customer's plan (y / n) ? : ")
    if changes=="y":
        found=0
        sname=input("\nEnter the Name to Search : ")                        #input name
        filein=open('customer_plan.txt','r+')
        for row in filein:
            name,status,plan,bill=row.split(',')
            if (name.lower()).strip()==(sname.lower()).strip():
                print("\nCustomer Name    : ",name)
                print("Plan Status      : ",status)
                print("Plan             : ",plan)
                print("Amount paid      : ",bill)
                found=1
                break
        if (found==0):
            print("\nEntered Name was not found in the Customer list......")
            filein.close()
        else:                                                                #this section takes input from the user and modifies customer plans in customer_plan.txt
            filein=open('customer_plan.txt','r+')
            fileout=open('sample_customer_plan.txt','w+',newline='')
            for row in filein:
                name,status,plan,bill=row.split(',')
                if name.lower()==sname.lower():
                    status_s=input("\nDo you want this customer's plan to be active ? (y / n) : ")
                    if status_s=="y":
                        status="ACTIVATED"
                        plan_s=input("\nEnter the plan the customer want \n\n1. Normal Plan (Rs 350 / month)\n2. HD Plan (Rs 650 / month)\n\nEnter input as 1 or 2 : ")
                        if plan_s=="1":
                            plan="Normal Plan"
                            bill="350"
                        elif plan_s=="2":
                            plan="HD Plan"
                            bill="650"
                    elif status_s=="n":
                        status="DEACTIVATED"
                        plan="________"
                        bill="________"
                    data=string.capwords(name)+","+status+","+plan+","+bill+"\n"
                    fileout.write(data)
                else:
                    fileout.write(row)
            filein.close()
            fileout.close()
            os.remove("customer_plan.txt")
            os.rename("sample_customer_plan.txt","customer_plan.txt")
            print("\nPlan Updation Successful........")
    elif changes=="n":
        print("\nNo changes have been made to the Plans")
    else:
        print("\nError : Wrong input...!")
