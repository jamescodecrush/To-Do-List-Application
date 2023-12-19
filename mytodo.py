#This is a to-do list application
# this application uses list, function, control sequence

#let creat an empty list to store our new to-do list items

from datetime import date

all_items = []
uncompleted_items = []
completed_item = []


# A function to add new items to the list

def add_item():
    global all_items, uncompleted_items
    while True:
        task = input("Add the name of the task or enter 0 to go to main menu: \n")
        if not task == '0':
         execution_date = input("Enter the date you want to execute this task formatted as YY-MM-DD  or enter 0 to skip: \n")
        else:
            break
        if execution_date == '0':
            task_date = "No date"
        else:
            execution_date = execution_date.split('-')
            year, month, day = [int(i) for i in execution_date]
            task_date = date(year, month, day)
            # print(task_date)
        for index, row in enumerate(all_items, 1):
          task_status = "....pending"  if row not in completed_item else "√"
          print(f"{index}, {'-'.join(map(str,row))}, task_status ")

        new_item = task, task_date
        all_items.append(new_item)
        uncompleted_items.append(new_item)
            
       
        
# a function ton display a list of tasks wth their status (completed or pending)

def display_tasks(sort_option = None):
    if len(all_items) <1:
        print("Sorry you have no tasks to display")
    if sort_option == "date":
        all_items.sort(key = lambda x: x[1])
    for index, row in enumerate(all_items, 1):
          task_status = "....pending"  if row not in completed_item else "√"
          print(f"{index}. {','.join(map(str,row))} {task_status} ")


def sorted_task():
    sort_option = input("Enter the sorting option you want (date or none) \n").lower()
    display_tasks(sort_option)
          
# Allowing users to mark task as completed

def mark_task_completed():
    if len(uncompleted_items) <1:
        print("Sorry you have no items here")
    global completed_item
    print("Which of the tasks whould you want to mark completed. Enter it's number. Example: 1 \n")
    for index, row in enumerate(uncompleted_items, 1):
        
            print(f"{index}. {', '.join(map(str, row))}")
    mark_item = int(input(">>>  "))

    if not mark_item > len(uncompleted_items):
        completed_item.append(uncompleted_items[mark_item-1])
        print("You have sucessfully marked ", row , " Completed")
        
    else:
        print("You entered a wrong option, please try again \n\n")
        mark_task_completed()
        
def delete_task():
    global all_items, uncompleted_items
    if len(all_items)<1:
        print("Sorry, there are no items here to delete")
    print("Which of the tasks whould you want to delet. Enter it's number. Example: 1 \n")
    for index, row in enumerate(all_items, 1):
        
            print(f"{index}, {'-'.join(map(str, row))}")
    del_item = int(input(">>>  "))
    if len(all_items) > del_item:
        for row in all_items:
            if row == all_items[del_item - 1]:
                deleted_item = [all_items.remove(row)]
        for row in uncompleted_items:
            if row == deleted_item:
                uncompleted_items.remove(row)
        del deleted_item[0]
        print("You have sucessfully deleted ", row)
        
    else:
        print("You entered a wrong option, please try again \n\n")
        delete_task()
    

    
def main():
    while True:
        print("Welcome to our to-do list application. Wha do you want to do ?  \n")
        user_choice = int(input("Please enter the option you want to do: \n"
            " 1. Add item to your to-do list \n"
            " 2. View all items in your to-do list \n"
            " 3. Mark item as completed \n"
            " 4. delete item from to-do list \n"
            " >>>  "))
        if user_choice <1 or user_choice > 4:
            print("You have entered an invalid option. Please try again")
        elif user_choice == 1:
            add_item()
        elif user_choice == 2:
            display_tasks()
        elif user_choice == 3:
            mark_task_completed()
        elif user_choice == 4:
            delete_task()
    

main()
        
    
 
