import sys
from storage import load_tasks, save_task

tasks = load_tasks() 

while True:
    print(f"1. List the tasks \n2. Add new task \n3. Exit \n") 
    user_request = input("Press 1, 2 or 3: ")
    if user_request == "1":
        if not tasks:
            print("There are no tasks yet.\n")
        else:
            for index, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status = "[✓]"
                else:
                    status = "[ ]"
                print(f"{index}. {status} {task['title']}")
            print("\n")
            request_2 = input(f"Would you like to: \n1. Delete a task \n2. Update task status \n3. Go back to menu \n")
            if request_2 == "1":
                try:
                    delete_task = int(input("\nWhich numbered task would you like to delete?: "))
                    index = delete_task - 1
                    tasks.pop(index)
                    print("Task deleted succesfully\n")
                    save_task(tasks)
                except (ValueError, TypeError, IndexError):
                    print("Invalid task number")
                
            elif request_2== "2":
                try:
                    update_task = int(input("\nWhich numbered task would you like to update?: "))
                    index = update_task - 1
                    tasks[index]["completed"] = True
                    print("Task updated succesfully\n")
                    save_task(tasks)
                except (ValueError, TypeError, IndexError):
                    print("Please enter task number")
            elif request_2 == "3":
                continue

    elif user_request == "2":
        add_task = input("New task: ")
        new_task = {"title": add_task, "completed": False}
        tasks.append(new_task)
        print("\nTask added succesfully.")
        save_task(tasks)
    elif user_request == "3":
        sys.exit()
    else:
        print("Please press 1, 2 or 3")

