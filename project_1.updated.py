#***********************************OM NAMA SHIVAYA **********************************
print("=======PERSONAL EXPENSE TRACKER========")
print()
name=input("Enter your name:")
budget=float(input("Enter your montly budget:"))
print()
total_expenses=int(input("How many expenses?:"))
print()
my_list=[]
for i in range(1,total_expenses+1):
    print(f"Expense {i}")
    Type=input("Name:")
    Amount=float(input("Amount:"))    
    category=input("Category:")
    my_list.append({
        "name":Type,
        "amount":Amount,
        "category":category
    })
    print()
print()
print("==== EXPENSE REPORT====")
print()
print(f"Name:{name}")
print(f"Monthly Budget:{budget}")
print()
for x in my_list:
    print(f"{x["name"]}    {x["amount"]}")
    print(f"{x["name"]}  {x["category"]}")
print()
total=0
dl=[]
for y in my_list:
    total+=y["amount"]
    dl.append(y["amount"])
print(f"Total spent:{total}")
print(f"Remaining Budget:{budget-total}")
if total_expenses!=0:
    k=max(dl)

for  j in my_list:
    if j["amount"]==k:
        z=j["name"]
        c=j["category"]
print(f"Highest Expense:{z} - {k}")
print(f"Highest valued category:{c}")
print()
if total>budget:
    print("WARNING!! BE IN YOUR SAFE LIMIT DON'T EXCEED YOUR BUDGET!")
else:
    print("You are within your Budget!")








      

    

