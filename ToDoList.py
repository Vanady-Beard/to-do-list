#Module 2: Mini-project | To-Do list Application
task = []

# add task function 

def add (task):
    user_input = (input ('Please Add A Task' + ' '))
    task.append(user_input)
    print (f'Great {user_input} have been added')
    
# view task function

def view (task):
    print (f'This is your list of tasks {task}')
    
# completed task function

def completed (task):
    user_complete = input(f'Which of these tasks do you want to mark as completed? {task}:  ')

    for i in range(len(task)): 
       if task[i] == user_complete:
           task[i]= user_complete + '  ' + ' X '
    #if user_complete in task:
    
    print (f'This {user_complete} is completed ')
    print (task)   
# deleted task function

def delete (task):  

    # user_delete = input (f"Which of these task would you like to delete? {task}  ")
    # if user_delete in task:
    #     task.remove (user_delete) 
    #     print(task) 
    # else: 
    #     print ('Item is not in task')

    try:
        user_delete = input (f"Which of these task would you like to delete? {task}")
        task.remove(user_delete)
        print(task)

    except:
        print (f'You do not have {user_delete} in your list') 

    

    

    
# quit task function

def quit (task):
    print ('Goodbye 👋🏽 Have A Great Day!')
    



def main (task): 
  while True:
   
    welcome_message = input ('''
            Welcome to the To-Do List App! 

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit 
         ''')    

    if welcome_message == '1':
        add(task)
    elif welcome_message == '2':
        view(task)
    elif welcome_message == '3':
        completed(task)
    elif welcome_message == '4':
        delete (task)
    elif welcome_message == '5':
        quit(task)
        break
    else:
        print('Please type a number to refer to the menu')
                
    
main (task)
                   