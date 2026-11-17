# def menu():
#     print("_________INVENTORY MANAGEMENT SYSTEM___________")
#     print("1. ADD PRODUCT")
#     print("2. DISPLAY ALL PRODUCTS")
#     print("3. SEARCH PRODUCT")
#     print("4. UPDATE PRODUCT")
#     print("5. DELETE PRODUCT")
#     print("6. LOW STOCK PRODUCTS")
#     print("7. SUMMARY OF PRODUCTS")
#     print("8. EXIT")
# items_in_shop=[]
# def add_product():
#     name=input("Enter the product name  to add product:")
#     if not name:
#         print("name cannot be empty please enter name of the product")
#         return
#     for item in items_in_shop:
#         if item["name"].casefold()==items_in_shop["name"].casefold():
#             items_in_shop["total_quantity"]+=1
#         else:
#             print(name,"Product will be added")
#     ID=input("Enter product ID to be added :")
#     for item in items_in_shop:#id can take like 26bcs034 also or int also
#         if ID.casefold()==item["id"].casefold():
#             print("ID already available please lable another ID to the product")
#             ID=input("Enter product ID to be added :")
#     else:
#         print("ID will be assigned to a product")
#     price=int(input("Enter the price of product in rupees to sell:"))
#     items_in_shop["availability"]="Available"
#     quantity=int(input("Enter the total number of quantity to be added :"))
#     if quantity>0:
#         items_in_shop.append({
#                 "name":name,
#                 "total_quantity":quantity,
#                 "price":price,
#                 "id":ID
#                 "avail"
#         })
#     else:
#         print("quantity zero so cannot be added") 
# def display_all_products():
#     if not items_in_shop:
#         print("NO items in a shop")
#     else:
#         print("Total products:",len(items_in_shop))
#         for item in items_in_shop:
#             print("\n-----Total products in our shop---------")
#             print("Name:",item["name"])
#             print("ID:",item["id"])
#             print("Price:",item["price"])
#             print("Quantity:",item["total_quantity"])
# def found_product(search):
#     found_id=False
#     found_name=False
#     if not search:
#         print("Enter name or ID to search it cannot be empty")
#     search=search.strip()
#     for item in items_in_shop:
#         if search.casefold()==item["id"].casefold():
#             found_id=True
#             print("Name:",item["name"])
#             print("ID:",item["id"])
#             print("Price:",item["price"])
#             print("Quantity:",item["total_quantity"])
            
#         elif search.casefold()==item["name"].casefold():
#             found_name=True
#             print("=====Your item is here")
#             print("Name:",item["name"])
#             print("ID:",item["id"])
#             print("Price:",item["price"])
#             print("Quantity:",item["total_quantuty"])
#             print("Available:",items_in_shop["availability"])
#     if found_id==False and found_name==False:
#         print("No product is available on this ID or name!")
# def search_product():
#     search=input("Enter product ID or name to view details")
#     found_product(search)

# def update_product():
#     return
# def delete_product():
#     return
# def low_stock_products():

#     return
# def summary_of_products():
#     return

# while True:
#     menu()
#     choice=int(input("Enter you choice for activity="))
#     if choice==1:
#         add_product()
#     if choice==2:
#         display_all_products()
#     if choice==3:
#         search_product()
#     if choice==4:
#         update_product()
#     if choice==5:
#         delete_product()
#     if choice==6:
#         low_stock_products()
#     if choice==7:
#         summary_of_products()
#     if choice==8:
#         break








