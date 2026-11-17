#----------OM NAMA SHIAVAYA ---------------
tasks=[]
def menu():
    print("------------------------------------------------------------------------")
    print("HAVE A JOURNEY IN A PERSONAL TRACKER")
    print("1. Add Task")
    print("2. Display All tasks")
    print("3. Search Tasks")
    print("4. Complete Tasks")
    print("5. Delete Tasks")
    print("6. Display Pending Tasks")
    print("7. Count tasks")
    print("8. Exit")
def add_task():
    task_name=input("Enter the Task name of the day:").strip()
    if not task_name:
        print("Task name cannot be empty")
        return
    for task in tasks:
        if task["Task name"].casefold()==task_name.casefold():
            print("A task with this name already exists")
            return
    task_status="Pending"
    task_description=input("Enter the task description:").strip()
    tasks.append({
            "Task name":task_name,
            "Task des":task_description,
            "Task stat":task_status
        })
def display():
    if not tasks:
        print("There are no tasks yet")
        return
    for i,task in enumerate(tasks):
        print("Task ID:",i+1)
        print("Task:",task["Task name"])
        print("Description:",task["Task des"])
        print("Task status:",task["Task stat"])
def find_task(search):
    search=search.strip()
    try:
        task_id=int(search)
    except ValueError:
        task_id=None
    if task_id is not None and 0 < task_id-1 < len(tasks):
        return task_id-1, tasks[task_id-1]
    for i, task in enumerate(tasks):
        if search.casefold()==task["Task name"].casefold():
            return i, task
    return None, None

def Search():
    search=input("Enter Task name or ID:")
    i, task=find_task(search)
    if task is None:
        print("Task not found")
        return
    print("Your task exists")
    print("Task ID:",i+1)
    print("Task:",task["Task name"])
    print("Description:",task["Task des"])
    print("Task status:",task["Task stat"])
def delete():
    search=input("Enter task name or Id:")
    i, task=find_task(search)
    if task is None:
        print("Task not found")
        return
    del tasks[i]
    print("Task deleted completely")
def status_update():
    print("Update your task to complete")
    search=input("Enter your Task name or ID:")
    i, task=find_task(search)
    if task is None:
        print("Task not found")
        return
    if task["Task stat"]=="Completed":
        print("Task is already completed")
        return
    task["Task stat"]="Completed"
    print("Task marked as completed")
def Display_pending():
    found=False
    for i,task in enumerate(tasks):
        if task["Task stat"]=="Pending":
            found=True
            print("Task ID:",i+1)
            print("Task:",task["Task name"])
            print("Description:",task["Task des"])
            print("Task status:",task["Task stat"])
    if not found:
        print("There are no pending tasks")
def count():
    count_P=0
    count_C=0
    print("Total no of tasks:",len(tasks))
    for i, task in enumerate(tasks,start=1):
        if task["Task stat"]=="Pending":
            count_P+=1
        elif task["Task stat"]=="Completed":
            count_C+=1
    print("Total Pending Tasks:",count_P)
    print("Total Completed Tasks:",count_C)
            
while True:
    menu()
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Please enter a number from 1 to 8")
        continue
    if choice==1:
        add_task()
    elif choice==2:
    
        display()
    elif choice==3:
        Search()
    elif choice==4:
        status_update()
    elif choice==5:
        delete()
    elif choice==6:
        Display_pending()
    elif choice==7:
        count()
    elif choice==8:
        break
    else:
        print("Invalid choice")
    

    


