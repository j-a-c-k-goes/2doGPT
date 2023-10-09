class Menu:
    menu = { 1: "Display all tasks.", 
             2: "Create new task.", 
             3: "Mark task as complete.", 
             4: "Mark all tasks complete.", 
             5: "Mark task incomplete.",
             6: "Mark all tasks incomplete", 
             7: "Display completed tasks.",
             8: "Display incomplete tasks.",
             9: "See menu",
             10: "Quit" }
    def __init__(self):
        pass
    def display_menu( self ):
        print( "\nTask List Menu Options" )
        print( "---------------------------" )
        for key, value in self.menu.items():
            print( key, "\t", value )
        print( "\n" )