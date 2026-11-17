#I have completed this project but the mistake i made here it is storing  values in multiple dictionary.
#in the next updated program i improved and created a list of dictionaries 
#next in the place of eval i updated to float and int.
#if the total_expenses are going to zero then k=max[dl] gives error i improved in updated project.


print("=======PERSONAL EXPENSE TRACKER========")
print()
name=input("Enter your name:")
budget=float(input("Enter your montly budget:"))
print()
total_expenses=int(input("How many expenses?:"))
print()
my_dict={}
my_dict_2={}
my_dict_3={}
for i in range(1,total_expenses+1):
    print(f"Expense {i}")
    Type=input("Name:")
    Amount=float(input("Amount:"))    
    category=input("Category:")
    my_dict[Type]=Amount
    my_dict_2[Type]=category
    my_dict_3[Amount]=category
    print()
print()
print("==== EXPENSE REPORT====")
print()
print(f"Name:{name}")
print(f"Monthly Budget:{budget}")
print()
for key,value in my_dict.items():
    print(f"{key}    {value}")
print()
total=0
dl=[]
for x,y in my_dict.items():
    total+=y
    dl.append(y)
print(f"Total spent:{total}")
print(f"Remaining Budget:{budget-total}")
k=max(dl)
for m,n in my_dict.items():
    if n==k:
        z=m
print(f"Highest Expense:{z} - {k}")
print()
if total>budget:
    print("WARNING!! BE IN YOUR SAFE LIMIT DON'T EXCEED YOUR BUDGET!")
else:
    print("You are within your Budget!")








      

    

