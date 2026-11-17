no_of_books=int(input("Enter the number of books you want to add:"))
my_collected_books=[]
print()
for i in range (1,no_of_books+1):    
    title=input("Enter the title of the book:")
    author=input("Enter the name of the Author:")
    i_d=int(input("Enter the ID of the book:"))
    total_copies=int(input("Enter the total copies of the book:"))
    my_collected_books.append({
        "title":title,
        "author":author,
        "id":i_d,
        "total_copies":total_copies
    })
    print("----------------------------------------------------------")
    print()
print("===================LIBRARY BOOKS====================")
print()
print()

for j in my_collected_books:
    print("TITLE:",j["title"])
    print("AUTHOIR:",j["author"])
    print("ID:",j["id"])
    print("TOTAL COPIES:",j["total_copies"])
    print("-------------------------------------------------------------")
if no_of_books!=0:
    highest_copies=max(my_collected_books,key=lambda x:x["total_copies"])
    print("THE BOOK WITH HIGHEST NUMBER OF COPIES IS:",highest_copies["title"],"-",highest_copies["total_copies"],"copies")
else:
    print("NO BOOKS ARE THERE IN THE LIBRSRY")
#search book program
my_book_titles=[]
my_book_authors=[]
my_book_ids=[]
for t in my_collected_books:
    my_book_titles.append(t["title"])
    my_book_authors.append(t["author"])
    my_book_ids.append(t["id"])


def menu():
    print("1. search book by title")
    print("2. search book by author")
    print("3. search book by id")
    print("4. exit")
while True:
    menu()
    choice=int(input("Enter your choice:"))
    if choice==1:
        search_book_with_title=input("Enter the name of the book you want to search:")
        
        for k in my_collected_books:
            
            if k["title"].casefold()==search_book_with_title.casefold():
                print("--------------BOOK FOUND!----------------")
            elif search_book_with_title in my_book_titles:
                pass
            elif search_book_with_title not in my_book_titles:
                print("Book is not available in a liberary!")
                break
            else:
                pass
                                
    elif choice==2:
        search_book_with_author=input("Enter the name of the author you want to search:")
        
        for l in my_collected_books:
           
            if l["author"]==search_book_with_author:   
                print("-------------------BOOK FOUND------------------")
            elif search_book_with_author in my_book_authors:
                pass      
            elif search_book_with_author not in my_book_authors:
                print("book not found in library")
                break
            else:
                pass                
    elif choice==3:
        search_book_with_id=int(input("Enter the ID of the book you want to search:"))
        
        for m in my_collected_books:
            if m["id"]==search_book_with_id:
                print("------------BOOK FOUND-------------")
            elif search_book_with_id  in my_book_ids:
                pass
            elif search_book_with_id not in my_book_ids:
                print("book not found")
                break
            else:
                pass
                
    elif choice==4:
        print("THANK YOU FOR USING THE LIBRARY MANAGEMENT SYSTEM")
        break
#improvemnts in this program is
#this i can use for a better code for search


#for book in my_collection_books:
#    if book["title"]==search_title------->(similarly)
#        print(book)
#else:
#    print("book not found")
#here else is for a for loop


# if a mtaching book is found break stops the loop
#if the loop finishes without break --->else runs.
