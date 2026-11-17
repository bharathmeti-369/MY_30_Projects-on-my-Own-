def menu():
    print("\n_________INVENTORY MANAGEMENT SYSTEM___________")
    print("1. ADD PRODUCT")
    print("2. DISPLAY ALL PRODUCTS")
    print("3. SEARCH PRODUCT")
    print("4. UPDATE PRODUCT")
    print("5. DELETE PRODUCT")
    print("6. LOW STOCK PRODUCTS")
    print("7. SUMMARY OF PRODUCTS")
    print("8. EXIT")
items_in_shop=[]
x="Available"
def add_product():
    name=input("Enter the product name  to add product:")
    name=name.strip()
    while True:
        try:
            quantity=int(input("Enter the total number of quantity to be added :"))
            if quantity>0:
                break
            else:
                print("Quantity must be a positive")
        except ValueError:
            print("Please enter a integer value")
    if not name:
        print("name cannot be empty please enter name of the product")
        return
    for item in items_in_shop:
        if item["name"].casefold()==name.casefold():
            item["total_quantity"]+=quantity
            item["availability"]="Available"
            return
    else:
        print(name,"Product will be added")
    while True:
        id_new=True
        ID=input("Enter product ID to be added :")
        if not ID :
            print("Please Label a ID to a product it cannot be empty")
        if ID:
            for item in items_in_shop:#id can take like 26bcs034 also or int also
                if ID.casefold()==item["id"].casefold():
                    print("ID already available please lable another ID to the product")
                    id_new=False
                    continue
        if id_new==True:
            print("This ID is assigned to a product")
            break 
    while True:
        
        try:
            price=int(input("Enter the price of product in rupees to sell:"))
        except ValueError:
            print("Please enter a valid integer")
        if price>0:
            break
        else:
            print("Price cannot be zero or a negative")
    if quantity>0:
        items_in_shop.append({
                "name":name,
                "total_quantity":quantity,
                "price":price,
                "id":ID,
                "availability":x
        })
    else:
        print("quantity zero so cannot be added") 
def display_all_products():
    print("\n-----Total products in our shop---------")
    if not items_in_shop:
        print("NO items in a shop")
    else:
        print("Total products:",len(items_in_shop))
        for item in items_in_shop:
            print("\n")
            print("---------------------")
            print("Name:",item["name"])
            print("ID:",item["id"])
            print("Price:",item["price"])
            print("Quantity:",item["total_quantity"])
            print("Availability:",item["availability"])
def found_product(search):
    found_id=False
    found_name=False
    if not search:
        print("Enter name or ID to search it cannot be empty")
        return
    search=search.strip()
    for item in items_in_shop:
        if search.casefold()==item["id"].casefold():
            found_id=True
            print("Name:",item["name"])
            print("ID:",item["id"])
            print("Price:",item["price"])
            print("Quantity:",item["total_quantity"])
            print("Availablity:",item["availability"])
        elif search.casefold()==item["name"].casefold():
            found_name=True
            print("=====Your item is here=====")
            print("Name:",item["name"])
            print("ID:",item["id"])
            print("Price:",item["price"])
            print("Quantity:",item["total_quantity"])
            print("Availablity:",item["availability"])
    if found_id==False and found_name==False:
        print("No product is available on this ID or name!")
def search_product():
    search=input("Enter product ID or name to view details:")
    found_product(search)
def update_product():
    #if a customer is ordered a any product or price of the product is increased or decreased updateing it 
    search=input("Enter product name or Id to update:")
    if not search:
        print("Please search product it cannot be empty")
        return
    def order_or_price():
        print("1. product is ordered")
        print("2. price is varied")
        print("3. Exit")
    while True:
        order_or_price()
        try:
            choice=int(input("Enter Your choice to update:"))
        except ValueError:
            print("Please enter a integer value")
            continue
        if choice==1:
            found_id=False
            found_name=False
            for item in items_in_shop:
                if search.casefold()==item["id"].casefold(): 
                    found_id=True
                    if item["total_quantity"]>0:
                        item["total_quantity"]-=1
                    if item["total_quantity"]==0:
                        print("-------------item is not in stock-----------")
                        item["availability"]="Not available"
                if search.casefold()==item["name"].casefold():
                    found_name=True
                    if item["total_quantity"]>0:
                        item["total_quantity"]-=1
                        print("---------Your order succesfully placed--------------")
                    if item["total_quantity"]==0:
                        print("next order cannot be done for this item ,it is out of stock")
                        item["availability"]="Not available"
            if found_id==False and found_name==False:
                print("\n----------------No product found with this id or name--------------") 
        elif choice==2:
            found_id=False
            found_name=False
            for item in items_in_shop:
                if search.casefold()==item["name"].casefold():
                    updated_price=int(input("Enter the price you want to update:"))
                    found_name=True
                    item["price"]=updated_price
                    print("\n----------------Price is updated succesfully--------------")
                elif search.casefold()==item["id"].casefold():
                    updated_price=int(input("Enter the price you want to update:"))
                    found_id=True
                    item["price"]=updated_price
                    print("\n-----------------Price is updated succesfully-----------------")
            if found_id==False and found_name==False:
                print("No product is found based on your search")
        elif choice==3:
            break
        else:
            print("choose a correct integer")
def delete_product():
    search=input("Enter name or ID of a product :")
    found_id=False
    found_name=False
    if not search:
        print("It cannot be empty please search id or name")
    if search:
        for item in items_in_shop:
            if search.casefold()==item["name"].casefold():
                found_name=True
                y=item
            elif search.casefold()==item["id"].casefold():
                found_id=True
                y=item
        items_in_shop.remove(y)
        if found_name==False and found_id==False:
            print("-------------------------No product is found please search a valid id or name-------------------")
def low_stock_products():
    low_stock_product=[]
    if len(items_in_shop)==0:
        print("---------------------There are no products available in this shop------------------------")
        return
    for item in items_in_shop:
        if 0<=item["total_quantity"]<5:
            low_stock_product.append(item)
    if len(low_stock_product)==0:
        print("---------------there are no less than 5 products in a shop------------------")
        return
    print("\n-----------------PRODUCTS ARE IN LOW QUANTITY-----------------")
    for item in low_stock_product:
        print("\n-------------------------------")
        print("ID:",item["id"])
        print("Name:",item["name"])
        print("Quantity:",item["total_quantity"])
        print("Avilability:",item["availability"])
def summary_of_products():
    total_product_in_our_shop=len(items_in_shop)
    print("Total Products In our shop:",total_product_in_our_shop)
    count=0
    availablity_stock_products=[]
    for item in items_in_shop:
        if item["availability"]==x:
            count+=item["total_quantity"]
            availablity_stock_products.append(item)
    print("\nTotal available items=",count)
    for item in availablity_stock_products:
        print()
        print("--------------------")
        print("ID:",item["id"])
        print("Name:",item["name"])
    
    total=0
    for item in items_in_shop:
        total+=(item["total_quantity"]*item["price"])
    print("Total items in Shop value:"," ",total,"rupees")
while True:
    menu()
    try:
        choice=int(input("Enter you choice for activity="))
    except ValueError:
        print("-------------------Enter a correct number to proceed------------------")
        continue
    if choice==1:
        add_product()
    elif choice==2:
        display_all_products()
    elif choice==3:
        search_product()
    elif choice==4:
        update_product()
    elif choice==5:
        delete_product()
    elif choice==6:
        low_stock_products()
    elif choice==7:
        summary_of_products()
    elif choice==8:
        break
    else:
        print("Please enter a valid choice")
