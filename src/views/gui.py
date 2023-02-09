import tkinter as tk
from tkinter import (Button, Entry, Frame, Label, OptionMenu, Radiobutton,
                     StringVar, Tk, ttk)

# Import Radiobutton and TreeView


class GUI:
    def __init__(self, parent):
        self.container = parent
        return

    def setup(self):
        """Call to setup the user interface"""
        self.create_widget()
        self.setup_layout()

    def create_widget(self):
        """Create a widgets in tkinter to first window"""
        self.langSelected = StringVar(None, "Language")
        # set lang list
        self.langList = ["English", "Português Brasil"]

        self.titleTxt = StringVar(None, "Contact Book")
        self.nameTxt = StringVar(None, "Name")
        self.lastNameTxt = StringVar(None, "Last Name")
        self.birthdayTxt = StringVar(None, "Birthday")
        self.phoneNumberTxt = StringVar(None, "Phone Number")
        self.addressTxt = StringVar(None, "Address")
        self.emailTxt = StringVar(None, "Email")
        self.searchTxt = StringVar(None, "Search")
        self.deleteTxt = StringVar(None, "Delete")
        self.alterTxt = StringVar(None, "Alter")
        self.saveTxt = StringVar(None, "Save")
        self.resultsTxt = StringVar(None, "Results")
        # set a default lang
        self.setLanguage("English")
        # Frames
        self.inforFrame = Frame(self.container, borderwidth=1,
                                highlightbackground="black")
        self.dataFrame = Frame(self.container, borderwidth=1,
                               highlightbackground="black")
        self.btnFrame = Frame(self.container)
        # Labels
        self.titleLb = Label(self.inforFrame, textvariable=self.titleTxt)
        self.nameLb = Label(self.dataFrame, textvariable=self.nameTxt)
        self.lastNameLb = Label(self.dataFrame, textvariable=self.lastNameTxt)
        self.birthdayLb = Label(self.dataFrame, textvariable=self.birthdayTxt)
        self.phoneNumberLb = Label(
            self.dataFrame, textvariable=self.phoneNumberTxt)
        self.addressLb = Label(self.dataFrame, textvariable=self.addressTxt)
        self.emailLb = Label(self.dataFrame, textvariable=self.emailTxt)

        # buttons
        self.searchBtn = Button(
            self.btnFrame,
            textvariable=self.searchTxt,
            command=self.searchPerson)
        self.deleteBtn = Button(
            self.btnFrame,
            textvariable=self.deleteTxt,
            command=self.deletePerson)
        self.alterBtn = Button(
            self.btnFrame,
            textvariable=self.alterTxt,
            command=self.alterPerson)
        self.saveBtn = Button(
            self.btnFrame,
            textvariable=self.saveTxt,
            command=self.savePerson)

        # Entrys
        self.nameEntry = Entry(self.dataFrame)
        self.lastNameEntry = Entry(self.dataFrame)
        self.birthdayEntry = Entry(self.dataFrame)
        self.phoneNumberEntry = Entry(self.dataFrame)
        self.addressEntry = Entry(self.dataFrame)
        self.emailEntry = Entry(self.dataFrame)

        # OptionMenu
        # setLanguage command to do
        self.langSelectOpt = OptionMenu(
            self.inforFrame,
            self.langSelected,
            *self.langList,
            command=self.setLanguage)

    def setup_layout(self):
        """Pack frames"""
        self.inforFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.dataFrame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.btnFrame.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
        # pack top frame
        self.titleLb.configure(font=('Arial bold', 20))
        self.titleLb.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        self.langSelectOpt.grid(row=0, column=3, padx=10, pady=10)

        # pack data frame
        self.nameLb.grid(row=1, column=0, padx=10, pady=10)
        self.nameEntry.configure(width=80)
        self.nameEntry.grid(row=1, column=1, padx=10, pady=10)
        self.lastNameLb.grid(row=2, column=0, padx=10, pady=10)
        self.lastNameEntry.configure(width=80)
        self.lastNameEntry.grid(row=2, column=1, padx=10, pady=10)
        self.birthdayLb.grid(row=3, column=0, padx=10, pady=10)
        self.birthdayEntry.configure(width=80)
        self.birthdayEntry.grid(row=3, column=1, padx=10, pady=10)
        self.phoneNumberLb.grid(row=4, column=0, padx=10, pady=10)
        self.phoneNumberEntry.configure(width=80)
        self.phoneNumberEntry.grid(row=4, column=1, padx=10, pady=10)
        self.emailLb.grid(row=5, column=0, padx=10, pady=10)
        self.emailEntry.configure(width=80)
        self.emailEntry.grid(row=5, column=1, padx=10, pady=10)
        self.addressLb.grid(row=6, column=0, padx=10, pady=10)
        self.addressEntry.configure(width=80)
        self.addressEntry.grid(row=6, column=1, padx=10, pady=10)

        # pack btn frame
        self.searchBtn.configure(width=10, height=2)
        self.searchBtn.grid(row=7, column=0, padx=10, pady=10)
        self.deleteBtn.configure(width=10, height=2)
        self.deleteBtn.grid(row=7, column=1, padx=10, pady=10)
        self.alterBtn.configure(width=10, height=2)
        self.alterBtn.grid(row=7, column=2, padx=10, pady=10)
        self.saveBtn.configure(width=10, height=2)
        self.saveBtn.grid(row=7, column=3, padx=10, pady=10)

    def create_second_window(self):
        self.container2 = tk.Toplevel()
        self.container2.title("Contact Book - Search")
        """Create widgets in tkinter to second window"""
        # Variables
        self.setFilter = StringVar(None, str(self.nameTxt.get()))
        self.choise = StringVar()
        # frame
        self.topFrame = Frame(self.container2)
        self.centerFrame = Frame(self.container2)
        self.bottomFrame = Frame(self.container2)

        # Labels
        self.searchLbl = Label(self.topFrame, textvariable=self.searchTxt)
        self.resultsLbl = Label(self.centerFrame, textvariable=self.resultsTxt)
        # todo
        self.filterLbl = Label(self.topFrame, textvariable=self.setFilter)

        # Filter Radio
        self.nameRdo = Radiobutton(
            self.topFrame,
            textvariable=self.nameTxt,
            variable=self.choise,
            value=str(self.nameTxt.get()),
            command=self.setFilterName)
        self.lastNameRdo = Radiobutton(
            self.topFrame,
            textvariable=self.lastNameTxt,
            variable=self.choise,
            value=str(self.lastNameTxt.get()),
            command=self.setFilterName)
        self.birthdayRdo = Radiobutton(
            self.topFrame,
            textvariable=self.birthdayTxt,
            variable=self.choise,
            value=str(self.birthdayTxt.get()),
            command=self.setFilterName)

        # Entry
        self.searchEntry = Entry(self.centerFrame)

        # button
        self.searchBtnN = Button(
            self.centerFrame,
            textvariable=self.searchTxt,
            command=self.alterPerson)

        # TreeView
        self.resultsTree = ttk.Treeview(self.bottomFrame)

    def setFilterName(self):
        radioSelect = str(self.choise.get())
        print(radioSelect)
        if(radioSelect == str(self.nameTxt.get())):
            self.setFilter.set(str(self.nameTxt.get()))
        elif(radioSelect == str(self.lastNameTxt.get())):
            self.setFilter.set(str(self.lastNameTxt.get()))
        elif(radioSelect == str(self.birthdayTxt.get())):
            self.setFilter.set(str(self.birthdayTxt.get()))
        else:
            pass

    def setup_layout_second_window(self):
        # pack frame
        self.topFrame.grid(row=0, column=0, padx=10, pady=10)
        self.centerFrame.grid(row=3, column=0, padx=10, pady=10)
        self.bottomFrame.grid(row=5, column=0, padx=10, pady=10)

        # pack into top frame
        self.searchLbl.grid(row=0, column=0, padx=10, pady=10)
        self.nameRdo.select()
        self.nameRdo.grid(row=0, column=2, padx=10, pady=10)
        self.lastNameRdo.grid(row=0, column=3, padx=10, pady=10)
        self.birthdayRdo.grid(row=0, column=4, padx=10, pady=10)

        # pack center frame
        self.filterLbl.grid(row=1, column=0, padx=1, pady=1)
        self.searchEntry.configure(width=40)
        self.searchEntry.grid(row=3, column=0)
        self.searchBtnN.grid(row=3, column=4, padx=10, pady=10)

        # pack bottom frame
        self.resultsLbl.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
        self.resultsTree.grid(row=5, column=0, rowspan=4,
                              columnspan=4, padx=10, pady=10)

    def setLanguage(self, language):
        """Define a lang: English is a default. Second lang is
        Português Brasil"""
        if(language == "English"):
            self.titleTxt.set("Contact Book")
            self.nameTxt.set("Name")
            self.lastNameTxt.set("Last Name")
            self.birthdayTxt.set("Birthday")
            self.phoneNumberTxt.set("Phone Number")
            self.addressTxt.set("Address")
            self.emailTxt.set("Email")
            self.searchTxt.set("Search")
            self.deleteTxt.set("Delete")
            self.alterTxt.set("Alter")
            self.saveTxt.set("Save")
            self.resultsTxt.set("Results")
        elif(language == "Português Brasil"):
            self.titleTxt.set("Livro de Contatos")
            self.nameTxt.set("Nome")
            self.lastNameTxt.set("Sobrenome")
            self.birthdayTxt.set("Data de Aniversário")
            self.phoneNumberTxt.set("Telefone")
            self.addressTxt.set("Endereço")
            self.emailTxt.set("Email")
            self.searchTxt.set("Buscar")
            self.deleteTxt.set("Excluir")
            self.alterTxt.set("Alterar")
            self.saveTxt.set("Salvar")
            self.resultsTxt.set("Resultados")
        else:
            pass
        return self

    def savePerson(self):
        print("Save")

    def deletePerson(self):
        print("Delete")

    def alterPerson(self):
        print("Alter")

    def searchPerson(self):
        self.create_second_window()
        self.setup_layout_second_window()


# test run
if __name__ == '__main__':
    mainwin = Tk()
    width = 650
    height = 450
    mainwin.geometry(f'{width}x{height}')
    mainwin.title('Contact Book')

    gui = GUI(mainwin)
    gui.setup()
    mainwin.mainloop()
