#-----------***********OM NAMA SHIVAYA***********------------
def contacts():
    print("1: Add contact")
    print("2: Search contact")
    print("3: Update contact")
    print("4: Delete contact")
    print("5: Display all contacts")
    print("6: Count contacts")
    print("7: Exit contact")
contact_details=[]
while True :
    contacts()
    choice=int(input("Enter your choice :"))
    if choice==1:

        name=input("Enter the name:")
        phone_number=int(input("Enter the phone number:"))
        #for the time being it is a considered as a phone number i cannot send otp i don,t know now at present situation
        email=input("Enter the email adress :")
        def verify_email():
            if email[-10::]=="@gamil.com":
                return "email is correct and move towards"         
        city=input("Enter your city:")

        if name in contact_details:
            print("Name already exists")
        elif not  verify_email:
            print("Email is not verified please enter a valid email id")
        else :
            duplicate=False
        contact_details.append({
            name:[phone_number,email,city]
        })
    elif choice==2:
        enter_phone_number=int(input("Enter Phone number(if don,t know phone number type 0:"))
        enter_name=input("Enter name(if you don,t know name type a(lower case)):")
        for x in  contact_details:
            for m_name,n_list in x.items():
                if n_list[0]==enter_phone_number or m_name.upper()==enter_name.upper():
                    print("name:",m_name)
                    print("Mobile_number:",n_list[0])
                    print("email:",n_list[1])
                    print("city:",n_list[2])
                else:
                    print("Contact not found")
    elif choice==3:#update status
        search_name=input("Enter the name you want to update or type a(lower case):")
        search_number=int(input("Enter th phone number or type 1:"))
        update=int(input("enter number what you have to update 1(name),2(phone_number),3(city),4(email):"))

        for y in contact_details:
            for k_name,l_list in y.items():
                if search_name.upper()==k_name.upper() or search_number==l_list[0]:
                    if update==1:
                        enter_new=input("Enter your new name:")
                        y[enter_new]=y.pop(k_name)
                    elif update==2:
                        new_phone_number=int(input("enter phone number:"))
                        l_list[0]=new_phone_number
                    elif update==3:
                        new_city=input("Enter city:")
                        l_list[2]=new_city
                    elif update==4:
                        new_email=input("Enter email:")
                        l_list[1]=new_email
                    else:
                        print("Please select any number from the above assigned number to a actions")
                print("congratulations contact updated")
            else:
                print("Contact not found")            
    elif choice==4:#delete
        name_d=input("Enter the name you want to delete(if don,t know simply write a):")
        phone_d=int(input("Enter the phone number you want to delete(if don,t know simply type 1):"))
        for z in contact_details:
            for i_name,j_list in z.items():
                if name_d.upper()==i_name.upper() or phone_d==l_list[0]:
                    contact_details.remove(z)
                else:
                    print(" enter stored name or phone number")
    elif choice==5:
        for i,v in enumerate(contact_details):
            for j_name,f_list in v.items():
                print("-----------Contact-------","=",i)
                print("Name:",j_name)
                print("Phone Number:",f_list[0])
                print("Email:",f_list[1])
                print("City:",f_list[2]) 
    elif choice==6:
        count_contact=len(contact_details)
        print("Total number if contacts stored in your account is :",count_contact)
    elif choice==7:
        break
    else:
        print("Invalid choice please enter a valid choice")          

