import os
import sys
import Menu
import Task
def clear_screen():
    os.system( "clear" )
if __name__ == "__main__":
    task_counter = 0
    Task = Task.Task()
    Menu = Menu.Menu()
    Menu.display_menu()
    Task.create_new_task( task_counter ); task_counter += 1
    Task.display_all_tasks()
    while True:
        menu_choice = int( input( "\nEnter a menu choice to do something else (enter 9 to see menu again): " ) )
        match menu_choice:
            case 1:
                clear_screen()
                Task.display_all_tasks()
            case 2:
                Task.create_new_task( task_counter )
                task_counter += 1
            case 3:
                clear_screen()
                Task.display_incomplete_tasks()
                try:
                    task_id = int( input( "\nEnter the id of the task you wish to mark complete: " ) )
                    Task.mark_task_complete( abs( task_id ) )
                except ValueError:
                    print( "Input invalid. the task_id has to be an integer." )
            case 4:
                Task.mark_all_tasks_complete()
            case 5:
                clear_screen()
                Task.display_completed_tasks()
                try:
                    task_id = int( input( "\nEnter the id of the task you wish to mark in-complete: " ) )
                    Task.mark_task_incomplete( task_id )
                except ValueError:
                    print( "Input invalid. the task_id has to be an integer." )
            case 6:
                Task.mark_all_tasks_incomplete()
            case 7: 
                clear_screen()
                Task.display_completed_tasks()
            case 8: 
                clear_screen()
                Task.display_incomplete_tasks()
            case 9:
                clear_screen()
                Menu.display_menu()
            case 10:
                print( "See you next time." )
                sys.exit(0)
            case _:
                print("Menu choice is likely invalid.\nOr there is no function to correspond with your choice.")