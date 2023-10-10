class Menu:
    menu = { 1: "Display all tasks.", 
             2: "Create new task.", 
             3: "Delete a task",
             4: "Mark task as complete.", 
             5: "Mark all tasks complete.", 
             6: "Mark task incomplete.",
             7: "Mark all tasks incomplete", 
             8: "Display completed tasks.",
             9: "Display incomplete tasks.",
             10: "See menu",
             11: "See task stats.",
             12: "Quit" }
    def __init__(self):
        pass
    def display_menu( self ):
        print( "\nTask List Menu Options" )
        print( "---------------------------" )
        for key, value in self.menu.items():
            print( key, "\t", value )
        print( "\n" )