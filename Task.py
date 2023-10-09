class Task:
    tasks = list()
    number_of_tasks_created = 0
    number_of_tasks_removed = 0
    number_of_tasks_completed = 0
    times_destroyed_completed_tasks = 0
    times_destroyed_incomplete_tasks = 0
    times_completed_everything = 0
    def __init__( self ):
        pass
    def create_new_task( self, task_counter=int):
        creating_new_task = True
        task_name = str( input( "Enter task: ") )
        self.set_task( task_counter, task_name, False )
        self.number_of_tasks_created += 1
    def display_number_of_tasks( self ):
        if ( self.number_of_tasks_created == 1 ):
            print( f"\nDisplaying { self.number_of_tasks_created } task." )
        else:
            print( f"\nDisplaying { self.number_of_tasks_created } tasks." )
    def display_all_tasks( self ):
        if ( len( self.get_tasks()) < 1 ):
            print( "The to-do list is empty." )
        else:
            self.display_number_of_tasks()
        for task in self.get_tasks():
            if task["task_status"] == False:
                print( f"({ task[ 'id' ] })\t[ x ]\t{ task[ 'task_name'] }" )
            else:
                print( f"({ task[ 'id' ] })\t[ ✓ ]\t{ task[ 'task_name' ] }" )
    def display_completed_tasks( self ):
        print( "\nDisplaying completed tasks only." )
        for task in self.get_tasks():
            task_completed = (task["task_status"] == True)
            if ( task_completed):
                print( f"({ task[ 'id' ] })\t[ ✓ ]\t{ task[ 'task_name' ] }" )
    def remove_completed_tasks( self ):
        print("\n Removing completed task from memory. I guess we only forget the things we complete.")
        tasks = self.get_tasks()
        for task in tasks:
            task_completed = (task["task_status"] == True)
            if ( task_completed ):
                tasks.remove( task_completed )
            self.times_destroyed_completed_tasks += 1
        self.set_tasks( tasks )
    def remove_incomplete_tasks( self ):
        print("\nYeah, let's just forget about the things we never accomplished.")
        tasks = self.get_tasks()
        for task in tasks:
            incomplete_task = ( task[ "task_status" ] == False )
            if ( incomplete_task ):
                tasks.remove( incomplete_task )
        self.times_destroyed_incomplete_tasks += 1
        self.set_tasks( tasks )
    def display_incomplete_tasks( self ):
        print( "\nDisplaying incomplete tasks. Hopefully, there aren't too many." )
        for task in self.get_tasks():
            task_incomplete = (task["task_status"] == False)
            if ( task_incomplete ):
                print( f"({ task[ 'id' ] })\t[ x ]\t{ task[ 'task_name'] }" )
    def mark_all_tasks_complete( self ):
        try:
            print( "Oh you are a power player, huh?" )
            tasks = self.get_tasks()
            for task in tasks:
                task["task_status"] = True
            self.times_completed_everything += 1
        except Exception:
            print( "A strange thing has happened. Maybe there are no tasks to mark." )
    def mark_all_tasks_incomplete( self ):
        try:
            print( "Wow. Life just became infinetely more difficult." )
            tasks = self.get_tasks()
            for task in tasks:
                task["task_status"] = False
        except Exception:
            print( "A strange thing has happened. Maybe there are no tasks to mark." )
    def mark_task_complete( self, task_to_mark_as_complete_id:int ):
        try:
            tasks = self.get_tasks()
            print("\nMarking task as complete. What an achievement." )
            for task in tasks:
                if ( task["id"] == task_to_mark_as_complete_id ):
                    task["task_status"] = True
            self.number_of_tasks_completed += 1
            self.set_tasks( tasks )
        except IndexError:
            print("There is no task with this id number.")
    def mark_task_incomplete( self, task_to_mark_as_incomplete_id:int ):
        try:
            tasks = self.get_tasks()
            print("\nMarking task as incomplete. Did we make a mistake? Or is this regression!?" )
            for task in tasks:
                if ( task[ "id" ] == task_to_mark_as_incomplete_id ):
                    task[ "task_status" ] = False
            self.set_tasks( tasks )
        except IndexError:
            print("There is no task with this id number.")
    def remove_task( self, task_removal_id:int):
        try:
            tasks = self.get_tasks()
            print("Removing task with id number ", task_removal_id )
            for task in tasks:
                if (task["id"] == task_removal_id):
                    tasks.remove( task )
            self.number_of_tasks_removed += 1
            self.set_tasks( tasks )
        except IndexError:
            print("There is no task with that id number.")
    def get_tasks(self):
        return list( self.tasks )
    def set_tasks( self, new_task_list:list ):
        self.tasks = new_task_list
    def set_task( self, new_task_id, new_task_name, new_task_status:bool ):
        if ( new_task_status != bool() ):
            print( "Unable to set new task. Task status must be a boolean value." )
            return
        else:
            self.tasks.append( { "id": new_task_id, 
                                 "task_name": new_task_name, 
                                 "task_status": new_task_status } )