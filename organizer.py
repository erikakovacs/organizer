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

def get_input_to_add(tasks):
    new_task = input("Enter your new task: ")
    add_task_to_list(tasks, new_task)

def add_task_to_list(tasks, new_task):
    tasks.append(new_task)

# Delete task from the list


def get_input_to_delete(tasks):
    index = input("Enter the number of the task to remove: ")
    try:
        delete_task(tasks, index)
    except TypeError:
        print("Please enter the number of the task: ")
    except:
        print("This task does not exist.")
    else:
        print("Task is successfully deleted.")


def delete_task(tasks, index):
    index = int(index) -1
    if index < len(tasks):
        del tasks[index]
    else: 
        raise Exception()
            

# Modify task

def get_input_to_modify(tasks):
    target_index = input("Enter the number to replace: ")
    new_value = input("Enter the new task: ")
    try:
        modify_task(tasks, target_index, new_value)
    except ValueError:
        print("Please enter the number of the task: ")
    except:
        print("This task does not exist.")
    else:
        print("Task replaced successfully.")


def modify_task(tasks, target_index, new_value):
    target_index = int(target_index) - 1
    if target_index < len(tasks):
        tasks[target_index] = new_value
    else:
        raise IndexError()
            


        

# Quit

def quit_from_app():
    print("See you later!")
    

# Choose an option

def get_input_to_option():
    pass

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
            delete_task(tasks)
            break
        elif option == modify:
            modify_task(tasks)
            break
        elif option == close:
            quit_from_app()
            break
            
        else:
            print("Invalid input!")
            option = input("Please, choose an option (1-4): ")


def main():
    say_hello()
    tasks = read_content()
    menu(tasks)
    write_content(tasks) 

if __name__ == "__main__":
    main()
 


