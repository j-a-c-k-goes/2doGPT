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
        menu_choice = int( input( "\nEnter a menu choice to do something else (enter 10 to see menu again): " ) )
        match menu_choice:
            # Display all tasks.
            case 1:
                clear_screen()
                Task.display_all_tasks()
            # Create new task.
            case 2:
                Task.create_new_task( task_counter )
                task_counter += 1
            # Remove a task.
            case 3:
                clear_screen()
                Task.display_all_tasks()
                try:
                    task_id = int( input( "\nEnter the id of the task you wish to mark complete: " ) )
                    Task.remove_task( abs( task_id ) )
                except ValueError:
                    print( "Input invalid. the task_id has to be an integer." )
            # Mark a task as complete.
            case 4:
                clear_screen()
                Task.display_incomplete_tasks()
                try:
                    task_id = int( input( "\nEnter the id of the task you wish to mark complete: " ) )
                    Task.mark_task_complete( abs( task_id ) )
                except ValueError:
                    print( "Input invalid. the task_id has to be an integer." )
            # Mark all tasks complete.
            case 5:
                Task.mark_all_tasks_complete()
            # Mark a task as incomplete.
            case 6:
                clear_screen()
                Task.display_completed_tasks()
                try:
                    task_id = int( input( "\nEnter the id of the task you wish to mark in-complete: " ) )
                    Task.mark_task_incomplete( task_id )
                except ValueError:
                    print( "Input invalid. the task_id has to be an integer." )
            # Mark all tasks as complete.
            case 7:
                Task.mark_all_tasks_incomplete()
            # Display only completed tasks.
            case 8: 
                clear_screen()
                Task.display_completed_tasks()
            # Display only un-done tasks.
            case 9: 
                clear_screen()
                Task.display_incomplete_tasks()
            # Display the menu.
            case 10:
                clear_screen()
                Menu.display_menu()
            # See task stats.
            case 11:
                clear_screen()
                Task.display_stats()
            # Quit.
            case 12:
                print( "See you next time." )
                sys.exit(0)
            case _:
                print("Menu choice is likely invalid.\nOr there is no function to correspond with your choice.")