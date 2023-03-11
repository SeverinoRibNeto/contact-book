# from tkinter import (Button, Entry, Frame, Label, OptionMenu, Radiobutton,
#                     StringVar, Tk, ttk)
from tkinter import Tk, messagebox
import tkinter as tk
from pubsub import pub  # Use to comunication
import sys
import os
if (os.path.join(os.getcwd(), 'src') not in sys.path):
    sys.path.append(os.path.join(os.getcwd(), 'src'))
from models.person import Person
from views.gui import GUI


class PersonController:
    """If alter 0, save; If alter 1, update table
    """
    alter = 0
    # Data header
    headerColumns = ['name', 'lastName', 'email',
                     'phoneNumber', 'address', 'birthday']

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
        pub.subscribe(self.configureViewTree, "Second_Windows_Created")
        pub.subscribe(self.set_filter, "Filter_Seted")

    def find_insert(self):
        id = self.person.lastIdInserted()  # Find Last data inserted
        self.person.id = id
        self.person.find()  # Find this data person
        self.insert_data_entries()  # Write data from Person into entries

    def delete_entry_data(self):
        self.view.nameEntry.delete(0, 'end')
        self.view.phoneNumberEntry.delete(0, "end")
        self.view.lastNameEntry.delete(0, "end")
        self.view.emailEntry.delete(0, "end")
        self.view.birthdayEntry.delete(0, "end")
        self.view.addressEntry.delete(0, "end")

    """Disable all entries
    """

    def disabled_entry(self):
        self.view.nameEntry.config(state='disabled')
        self.view.phoneNumberEntry.config(state='disabled')
        self.view.lastNameEntry.config(state='disabled')
        self.view.emailEntry.config(state='disabled')
        self.view.birthdayEntry.config(state='disabled')
        self.view.addressEntry.config(state='disabled')

        """Enable all entries
        """

    def enable_entry(self):
        self.view.nameEntry.config(state='normal')
        self.view.phoneNumberEntry.config(state='normal')
        self.view.lastNameEntry.config(state='normal')
        self.view.emailEntry.config(state='normal')
        self.view.birthdayEntry.config(state='normal')
        self.view.addressEntry.config(state='normal')

    def insert_data_entries(self):
        self.view.nameEntry.insert(0, str(self.person.name))
        self.view.phoneNumberEntry.insert(0, str(self.person.phoneNumber))
        self.view.lastNameEntry.insert(0, str(self.person.lastName))
        self.view.emailEntry.insert(0, str(self.person.email))
        self.view.birthdayEntry.insert(0, str(self.person.birthday))
        self.view.addressEntry.insert(0, str(self.person.address))

    # Save person
    def save_person(self):
        if (self.alter == 0):
            self.person = Person(name=str(self.view.nameEntry.get()),
                                 phoneNumber=str(
                                     self.view.phoneNumberEntry.get()),
                                 lastName=str(self.view.lastNameEntry.get()),
                                 email=str(self.view.emailEntry.get()),
                                 address=str(self.view.addressEntry.get()),
                                 birthday=str(self.view.birthdayEntry.get()))
            try:
                self.person.save()
                messagebox.showinfo(
                    title="Saved", message="Saved successfully")
                self.disabled_entry()
            except Exception as e:
                print(e)
        else:
            self.person.name = str(self.view.nameEntry.get())
            self.person.phoneNumber = str(self.view.phoneNumberEntry.get())
            self.person.lastName = str(self.view.lastNameEntry.get())
            self.person.email = str(self.view.emailEntry.get())
            self.person.address = str(self.view.addressEntry.get())
            self.person.birthday = str(self.view.birthdayEntry.get())
            self.person.alter()
            self.delete_entry_data()
            self.insert_data_entries()
            self.alter = 0  # Alter data variable to 0, to save in next time
        print("Controller - Save")

    def delete_person(self):
        try:
            self.person.delete()
        except Exception as e:
            messagebox.showerror(title="Error", message=e)
        self.delete_entry_data()
        self.find_insert()
        self.disabled_entry()
        print("Controller - Delete")

    def alter_person(self):
        self.enable_entry()
        self.alter = 1  # Set a variable to update the person in save
        print("Controller - Alter")

    # Set a Filter variable
    def set_filter(self):
        self.filter = self.view.setFilter.get()

    def get_person(self):
        self.deleteResultsTreeView()
        self.person.name = str(self.view.searchEntry.get())
        self.addResultsToViewTree(self.person.findByName(
            str(self.view.searchEntry.get())))
        print("Controller - Find")

    # Add results to Tree View
    def addResultsToViewTree(self, data):
        for contact in data:
            self.view.resultsTree.insert('', tk.END, values=contact)

    # Delete elements of Tree View
    def deleteResultsTreeView(self):
        for item in self.view.resultsTree.get_children():
            self.view.resultsTree.delete(item)

    # Configure a Tree View Headings
    def configureViewTree(self):
        columns = self.headerColumns
        columns.insert(0, 'id')
        self.view.resultsTree.configure(
            columns=columns, show='headings')
        self.view.resultsTree.heading(
            'id', text="Id")
        self.view.resultsTree.column('id', minwidth=0, width=30)
        self.view.resultsTree.heading(
            'name', text=str(self.view.nameTxt.get()))
        self.view.resultsTree.column('name', minwidth=0, width=150)
        self.view.resultsTree.heading(
            'lastName', text=str(self.view.lastNameTxt.get()))
        self.view.resultsTree.column('lastName', minwidth=0, width=150)
        self.view.resultsTree.heading(
            'email', text=str(self.view.emailTxt.get()))
        self.view.resultsTree.column('email', minwidth=0, width=150)
        self.view.resultsTree.heading(
            'phoneNumber', text=str(self.view.phoneNumberTxt.get()))
        self.view.resultsTree.column('phoneNumber', minwidth=0, width=90)
        self.view.resultsTree.heading(
            'address', text=str(self.view.addressTxt.get()))
        self.view.resultsTree.column('address', minwidth=0, width=180)
        self.view.resultsTree.heading(
            'birthday', text=str(self.view.birthdayTxt.get()))
        self.view.resultsTree.column('birthday', minwidth=0, width=80)
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
