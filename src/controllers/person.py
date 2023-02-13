# from tkinter import (Button, Entry, Frame, Label, OptionMenu, Radiobutton,
#                     StringVar, Tk, ttk)
from tkinter import Tk
import tkinter as tk
from pubsub import pub  # Use to comunication
import sys
import os
if (os.path.join(os.getcwd(), 'src') not in sys.path):
    sys.path.append(os.path.join(os.getcwd(), 'src'))
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
        pub.subscribe(self.get_person, "Search_Button_Pressed")

    def save_person(self):
        self.person = Person(name=str(self.view.nameEntry.get()),
                             phoneNumber=str(self.view.phoneNumberEntry.get()),
                             lastName=str(self.view.lastNameEntry.get()),
                             email=str(self.view.emailEntry.get()),
                             address=str(self.view.addressEntry.get()),
                             birthday=str(self.view.birthdayEntry.get()))
        self.person.save()
        print("Controller - Save")

    def delete_person(self):
        self.person = Person(name=str(self.view.nameEntry.get()),
                             phoneNumber=str(self.view.phoneNumberEntry.get()),
                             lastName=str(self.view.lastNameEntry.get()),
                             email=str(self.view.emailEntry.get()),
                             address=str(self.view.addressEntry.get()),
                             birthday=str(self.view.birthdayEntry.get()))
        self.person.delete()
        print("Controller - Delete")

    def alter_person(self):
        self.person = Person(name=str(self.view.nameEntry.get()),
                             phoneNumber=str(self.view.phoneNumberEntry.get()),
                             lastName=str(self.view.lastNameEntry.get()),
                             email=str(self.view.emailEntry.get()),
                             address=str(self.view.addressEntry.get()),
                             birthday=str(self.view.birthdayEntry.get()))
        print("Controller - Alter")

    def get_person(self):
        self.person.name = str(self.view.searchEntry.get())
        self.configureViewTree()
        self.addResultsToViewTree(self.person.findByName(
            str(self.view.searchEntry.get())))
        print("Controller - Find")

    def addResultsToViewTree(self, data):
        for contact in data:
            self.view.resultsTree.insert('', tk.END, values=contact)

    def configureViewTree(self):
        columns = self.person.headerColumns
        columns.insert(0, 'id')
        self.view.resultsTree.configure(
            columns=columns, show='headings')
        self.view.resultsTree.heading(
            'id', text="Id")
        self.view.resultsTree.heading(
            'name', text=str(self.view.nameTxt.get()))
        self.view.resultsTree.heading(
            'lastName', text=str(self.view.lastNameTxt.get()))
        self.view.resultsTree.heading(
            'email', text=str(self.view.emailTxt.get()))
        self.view.resultsTree.heading(
            'phoneNumber', text=str(self.view.phoneNumberTxt.get()))
        self.view.resultsTree.heading(
            'address', text=str(self.view.addressTxt.get()))
        self.view.resultsTree.heading(
            'birthday', text=str(self.view.birthdayTxt.get()))
        return


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
