from organizer_variables import * 
import json

# Say hello

def say_hello():
    print("Hello, Erika!" + "\n")

# Open the file

def read_content():
    file = open(filepath, "r")
    tasks = json.load(file)
    file.close()
    return tasks

def write_content(tasks):
    file = open(filepath, "w", encoding = 'utf8')
    json.dump(tasks, file, ensure_ascii=False)


# Print tasks

def print_tasks(tasks):
    for i, item in enumerate(tasks):
        print(f'{i+1}. {item}')    
    print("\n")


# Add task to the list

def add_task_to_list(tasks):
    new_task = input("Enter your new task: ")
    tasks.append(new_task)

# Delete task from the list

def delete_task():
    try:
        index = int(input("Enter the number of the task to remove: ")) -1
        if index < len(tasks):
            del tasks[index]
            print("Task is successfully deleted.")
        else:
            print("This task does not exist.")
    except:
        print("Please enter the number of the task: ")
    

# Modify task

def modify_task():
    try:
        target_index = int(input("Enter the number to replace: ")) - 1
        if target_index < len(tasks):
            new_value = input("Enter the new task: ")
            tasks[target_index] = new_value
            print(f"Task replaced to {new_value}")
        else:
            print("This task does not exist.")
    except:
        print("Enter the number to replace: ")


        

# Quit

def quit_from_app():
    print("See you later!")
    

# Choose an option

def show_option(tasks):
    print("1. Add new task")
    print("2. Delete task")
    print("3. Modify task")
    print("4. Quit\n")
    print("Your tasks: \n")
    print_tasks(tasks)
    return input("Please, choose an option (1-4): ")
    

def menu(tasks):
    while True:
        option = show_option(tasks) 
        if option == add:
            add_task_to_list(tasks)
            break
        elif option == delete:
            delete_task()
            break
        elif option == modify:
            modify_task()
            break
        elif option == close:
            quit_from_app()
            break
            
        else:
            print("Invalid input!")
            option = input("Please, choose an option (1-4): ")
   
 
say_hello()
tasks = read_content()
menu(tasks)
write_content(tasks)

