from tkinter import Tk
from pubsub import pub  # Use to comunication
import sys
import os
if (os.path.join(os.getcwd(), 'src') not in sys.path):
    sys.path.append(os.path.join(os.getcwd(), 'src'))
    print("Path Added")
from models.person import Person
from views.gui import GUI


class PersonController:

    def __init__(self, main_window):  # main_window is tkinter main window
        # variables
        self.main_window = main_window
        self.person = Person()  # point to Person Object
        self.view = GUI(main_window)  # point to GUI interface
        self.view.setup()  # Configurate a view to show window

        pub.subscribe(self.save_person, "Save_Button_Pressed")
        pub.subscribe(self.delete_person, "Delete_Button_Pressed")
        pub.subscribe(self.alter_person, "Alter_Button_Pressed")

    def save_person(self):
        print("Controller - Save")

    def delete_person(self):
        print("Controller - Delete")

    def alter_person(self):
        print("Controller - Alter")


# App entry to main method
if __name__ == '__main__':
    # Create tk
    mainwin = Tk()
    width = 650
    height = 450
    mainwin.geometry(f'{width}x{height}')
    mainwin.title('Contact Book')

    app = PersonController(mainwin)
    mainwin.mainloop()
