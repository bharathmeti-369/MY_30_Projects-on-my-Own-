#---------OM NAMA SHIVAYA ---------------
contacts=[]
def show_menu():
    print("\n--------CONTACT BOOK-----------")
    print("1 : ADD CONTACT")
    print("2: SEARCH CINTACT")
    print("3: UPDATE CONTACT")
    print("4:DELETE CONTACT")
    print("5: DISPLAY_ALL_CONTACTS")
    print("6: COUNT CONTACTS")
    print("7: EXIT")
def add_contacts():
    name=input("Enter name:")
    num=input("Enter  phone number:")
    email=input("Enter email: ")
    city=input("Enter city:")
    if not email.endswith("@gmail.com"):
        print("Invalid email")
        return
    for contact in contacts:
        if contact["phone"]==num:
            print("The Phone number is already exists ")
            return
    contacts.append({
        "name":name,
        "phone":num,
        "email":email,
        "city":city
    })
    print("CONTACT ADDED SUCCESFULLY")
def search_contact():
    search=input("Enter name or a phone number:")
    found=False
    for contact in contacts:
        if (contact["name"].lower==search.lower() or contact["phone"]==search):
            print("\nCONTACT FOUND")
            found=True
            break
        if not found:
            print("Contact is not there")
def update_contacts():
    search=input("Enter name or a phone_number:")
    found=False
    for contact in contacts:
        if (contact["name"].lower==search.lower() or contact["phone"]==search):
            print("\n CONTACT FOUND")
            found=True
            print("1.Update name")
            print("2.Update Phone number")
            print("3.Update email")
            print("4.Update city")
            choice=int(input("Enter your choice:"))
            if choice==1:
                contact["name"]=input("Enter name:")
            elif choice==2:
                new_phone=input("Enter new phone number:")
                duplicate=False
                for other in contacts:
                    if (other["phone"]==new_phone and other is not contact):
                        duplicate=True
                        break
                if duplicate:
                    print("Phone number Already exists!")
                    return
                contact["phone"]=new_phone
            elif choice==3:
                new_email=input("Enter Email:")
                if new_email.endswith("@gmail.com"):
                    contact["email"]=new_email
                else:
                    print("INVALID EMAIL!")
            elif choice==4:
                contact["city"]=input("enter City:")
            else:
                print("Invalid update choice!")
                return
            print("Contact updated succesfully")
            break
    if not found:
        print("Contact not Found ")
def delete_contact():
    search=input("Enter phone number or name:")
    found_contact=None
    for contact in contacts:
        if (contact["name"].lower==search.lower() or contact["phone"]==search):
            found_contact=contact
            break
    if found_contact is not None:
        contacts.remove(found_contact)
        print("Contact deleted succesfully")
    else:
        print("Contact not found")
def display_contacts():
    if len(contacts)==0:
        print("contact book is empty")
        return
    for index,contact in enumerate(contacts,start=1):
        print(f"\n--------contact {index}--------")
        print("Name:",contact["name"])
        print("Phone number:",contact["phone"])
        print("Email:",contact["email"])
        print("City:",contact["city"])
def count_contacts():
    print("Total Contacts:",len(contacts))
while True:
    show_menu()
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_contacts()
    elif choice==2:
        search_contact()
    elif choice==3:
        update_contacts()
    elif choice==4:
        delete_contact()
    elif choice==5:
        display_contacts()
    elif choice==6:
        count_contacts()
    elif choice==7:
        print("Thank you for using Contact Book!")
        break
    else:
        print("Inavlid choicce please select a Valid choice!")








